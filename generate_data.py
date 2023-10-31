import pandas as pd
import random
import textwrap
import os
from dummy import data

import random
import textwrap

class RadiologyReportGenerator:
    def __init__(self):
        self.template = """
        CT Onco Lung Mass

        Clinical information: Patient presents with confirmed stage IV NSCLC. 

        Comparison: None.

        Findings:
        Lung mass
        Size: {:.1f} cm
        Volume: {:.1f} cm3
        Location: Lung (series {}, image {})
        Shape: Spiculated
        Internal consistency: Centrally calcified

        Local extent:
        Pleural surface: No involvement.
        Chest wall: No involvement.
        Airway: No involvement.
        Vessels: {}
        Nerves: No involvement.

        Regional extent:
        Lymph nodes: {}
        Short Axis Lymph Node: {} mm

        Distant metastases (chest and upper abdomen): None.

        Other findings: Non-target lesion located in the {}, with a diameter of {} mm.

        Impression: Further evaluation and follow-up are recommended.
        """
    
    def generate_report(self, row):
        series_number = random.randint(1, 30)
        image_number = random.randint(1, 150)
        vessels_text = "No involvement." if row['Tumor_Invading_Blood_Vessels'] == "Tumor Not Invading" else "Involvement detected."
        lymph_nodes_text = "No adenopathy." if row['Short_Axis_Lymph_Node'] < 10 else "Adenopathy detected."
        
        report = self.template.format(
            row['Target_Lesion_Length'] / 10,
            (4 / 3) * 3.1415 * ((row['Target_Lesion_Length'] / 2) / 10) ** 3,
            series_number, image_number,
            vessels_text,
            lymph_nodes_text,
            row['Short_Axis_Lymph_Node'],
            row['Non_Target_Lesion_Location'],
            row['Non_Target_Lesion_Diameter']
        )
        
        return textwrap.dedent(report), series_number, image_number, vessels_text, lymph_nodes_text

    def generate_labels(self, text, row, series_number, image_number, vessels_text, lymph_nodes_text):
        labels = ['O'] * len(text)
        
        # Size
        size_text = "{:.1f} cm".format(row['Target_Lesion_Length'] / 10)
        size_start = text.find(size_text)
        size_end = size_start + len(size_text)
        if size_start != -1:
            labels[size_start:size_end] = ['B-SIZE'] + ['I-SIZE'] * (size_end - size_start - 1)

        # Location
        location_text = "Location: Lung (series {}, image {})".format(series_number, image_number)
        location_start = text.find(location_text)
        location_end = location_start + len(location_text)
        if location_start != -1:
            labels[location_start:location_end] = ['B-LOCATION'] + ['I-LOCATION'] * (location_end - location_start - 1)
        
        # Vessels
        vessels_start = text.find(vessels_text)
        vessels_end = vessels_start + len(vessels_text)
        if vessels_start != -1:
            labels[vessels_start:vessels_end] = ['B-VESSELS'] + ['I-VESSELS'] * (vessels_end - vessels_start - 1)
        
        # Lymph Nodes
        lymph_nodes_start = text.find(lymph_nodes_text)
        lymph_nodes_end = lymph_nodes_start + len(lymph_nodes_text)
        if lymph_nodes_start != -1:
            labels[lymph_nodes_start:lymph_nodes_end] = ['B-LYMPH-NODES'] + ['I-LYMPH-NODES'] * (lymph_nodes_end - lymph_nodes_start - 1)
        
        # Short Axis Lymph Node
        short_axis_text = "{} mm".format(row['Short_Axis_Lymph_Node'])
        short_axis_start = text.find(short_axis_text)
        short_axis_end = short_axis_start + len(short_axis_text)
        if short_axis_start != -1:
            labels[short_axis_start:short_axis_end] = ['B-SHORT-AXIS-LN'] + ['I-SHORT-AXIS-LN'] * (short_axis_end - short_axis_start - 1)
        
        # Non-Target Lesion
        non_target_lesion_text = "Non-target lesion located in the {}, with a diameter of {} mm.".format(
            row['Non_Target_Lesion_Location'], row['Non_Target_Lesion_Diameter']
        )
        non_target_lesion_start = text.find(non_target_lesion_text)
        non_target_lesion_end = non_target_lesion_start + len(non_target_lesion_text)
        if non_target_lesion_start != -1:
            labels[non_target_lesion_start:non_target_lesion_end] = ['B-NON-TARGET-LESION'] + ['I-NON-TARGET-LESION'] * (non_target_lesion_end - non_target_lesion_start - 1)

        return labels


# Usage example:
generator = RadiologyReportGenerator()

row = {
    'Target_Lesion_Length': 35,
    'Tumor_Invading_Blood_Vessels': "Tumor Invading",
    'Short_Axis_Lymph_Node': 12,
    'Non_Target_Lesion_Location': "liver",
    'Non_Target_Lesion_Diameter': 22
}
# report, series_number, image_number, vessels_text, lymph_nodes_text = generator.generate_report(row)
# labels = generator.generate_labels(report, row, series_number, image_number, vessels_text, lymph_nodes_text)
# print(report)
# print(labels)


from sklearn.model_selection import train_test_split
import csv

# Instantiate the RadiologyReportGenerator
generator = RadiologyReportGenerator()

# Split the data into training and testing sets
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

# Generate radiology reports and labels, then save each as a row in the train and test CSV files
for dataset, data in [('train', train_data), ('test', test_data)]:
    with open(f'{dataset}.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['report_id', 'report_text', 'labeled_text'])
        
        for index, row in data.iterrows():
            # Skip rows with missing data
            if row.isnull().any():
                continue
            report, series_number, image_number, vessels_text, lymph_nodes_text = generator.generate_report(row)
            labels = generator.generate_labels(report, row, series_number, image_number, vessels_text, lymph_nodes_text)

            writer.writerow([index, report, ' '.join(labels)])

    # Read the csv files, drop the empty rows, and save again
    df = pd.read_csv(f'{dataset}.csv')
    df.dropna(inplace=True)
    df.to_csv(f'{dataset}.csv', index=False)

