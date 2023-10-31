## DISCLAIMER: THE FOLLOWING DATA ARE NOT REAL AND WERE PREPARED BASED ON THE SELECTION CRITERIA OF THE TRIAL BELOW

##################################
# Title: A Study of Carboplatin, Pemetrexed Plus Placebo vs Carboplatin, Pemetrexed Plus 1 or 2 Truncated Courses of Demcizumab in Subjects With Non-Squamous Non-Small Cell Lung Cancer (DENALI)
# ClinicalTrials.gov ID: NCT02259582
# Sponsor: OncoMed Pharmaceuticals, Inc.
# Information provided by: Mereo BioPharma (OncoMed Pharmaceuticals, Inc.) (Responsible Party)
# Last Update Posted: 2020-09-09
##################################

import pandas as pd
import random

# Define the number of records
num_records = 100

# Create random data for each criterion

# Main Inclusion Criteria
signed_icf = [random.choice(["John Doe", "Jane Smith"]) for _ in range(num_records)]
confirmed_nsclc = [random.choice(["Histologically Confirmed", "N/A"]) for _ in range(num_records)]
availability_ffpe = [random.choice(["Fresh Biopsy", "Unavailable"]) for _ in range(num_records)]
age = [random.randint(18, 80) for _ in range(num_records)]

# ECOG: 0 - 5; include 0 or 1
# Grade	Description of patient
# 0	Fully active, able to carry on all predisease performance without restriction
# 1	Restricted in physically strenuous activity but ambulatory and able to carry out work of a light or sedentary nature, e.g., light housework, office work
# 2	Ambulatory and capable of all self-care but unable to carry out any work activities; up and about more than 50% of waking hours
# 3	Capable of only limited self-care; confined to bed or chair more than 50% of waking hours
# 4	Completely disabled; cannot carry on any self-care; totally confined to bed or chair
# 5	Dead
ecog_status = [random.choice([0, 1, 2]) for _ in range(num_records)]

# RECIST v1.1
# target lesion--tumor length in mm
target_lesion_length = [random.randint(1, 100) for _ in range(num_records)]
# target lesion--number of lesions per tumor lesion
num_lesions_per_tumor = [random.randint(1, 10) for _ in range(num_records)]
# target lesion--short axis lymph node in mm
short_axis_lymph_node = [random.randint(1, 50) for _ in range(num_records)]
# non-target lesion--location/organ (brain,lymph nodes, bones, liver)
non_target_lesion_location = [random.choice(["Brain", "Lymph Nodes", "Bones", "Liver"]) for _ in range(num_records)]
# non-target lesion--diameter in mm
non_target_lesion_diameter = [random.randint(1, 100) for _ in range(num_records)]
# non-target lesion--absence or presence of non-measurables like pleural fluid, ascites, lymphangitis
non_target_lesion_nonmeasurables = [random.choice(["Pleural Fluid", "Ascites", "Lymphangitis", "None"]) for _ in range(num_records)]

# Contraception
women_contraception = [random.choice(["IUD","OCP","Depo","N/A"]) for _ in range(num_records)]

# SOFAS
paO2_FiO2 = [random.randint(100, 400) for _ in range(num_records)]
platelets = [random.randint(20, 150) for _ in range(num_records)]
bilirubin = [round(random.uniform(1.2, 12), 1) for _ in range(num_records)]
cardiovascular = [random.choice(["MAP above 70", "MAP equal to or below 70", "Dopamine (Dop) less than or equal to 5 or dobutamine (any dose)", "Dopamine (Dop) greater than 5 but Epinephrine (Epi) less than or equal to 0.1", "Epinephrine (Epi) greater than 0.1"]) for _ in range(num_records)]
glasgow_coma_scale = [random.randint(3, 15) for _ in range(num_records)]
creatinine = [round(random.uniform(0.5, 5.5), 2) for _ in range(num_records)]

# Main Exclusion Criteria
mixed_nsclc = [random.choice(["Mixed NSCLC", "Pure NSCLC", "N/A"]) for _ in range(num_records)]
known_egfr_alk = [random.choice(["EGFR Mutation", "ALK Translocation", "None"]) for _ in range(num_records)]
prior_therapy = [random.choice(["Chemotherapy", "Radiotherapy", "None"]) for _ in range(num_records)]
tumor_invading_blood_vessels = [random.choice(["Tumor Encroaching Pulmonary Vein", "Tumor Not Invading", "N/A"]) for _ in range(num_records)]
brain_metastases = [random.choice(["Brain Metastases Present", "No Brain Metastases", "N/A"]) for _ in range(num_records)]
other_malignancies = [random.choice(["Breast Cancer", "Prostate Cancer", "None"]) for _ in range(num_records)]
allergic_reaction = [random.choice(["Anaphylaxis to Humanized Antibody", "No Allergic Reaction", "N/A"]) for _ in range(num_records)]
intercurrent_illness = [random.choice(["Advanced Heart Failure", "No Significant Illness", "N/A"]) for _ in range(num_records)]
recent_hemoptysis = [random.choice(["Yes","No"]) for _ in range(num_records)] 
major_surgery = [random.choice(["Gallbladder Removal", "No Surgery", "N/A"]) for _ in range(num_records)]

data = pd.DataFrame({
    'Signed_ICF': signed_icf,
    'Confirmed_Stage_IV_NSCLC': confirmed_nsclc,
    'Availability_FFPE': availability_ffpe,
    'Age': age,
    'ECOG_Status': ecog_status,
    'Target_Lesion_Length': target_lesion_length,
    'Num_Lesions_Per_Tumor': num_lesions_per_tumor,
    'Short_Axis_Lymph_Node': short_axis_lymph_node,
    'Non_Target_Lesion_Location': non_target_lesion_location,
    'Non_Target_Lesion_Diameter': non_target_lesion_diameter,
    'Non_Target_Lesion_Nonmeasurables': non_target_lesion_nonmeasurables,
    # 'Adequate_Organ_Function': adequate_organ_function,
    'Women_Contraception': women_contraception,
    'PaO2_FiO2': paO2_FiO2,
    'Platelets': platelets,
    'Bilirubin': bilirubin,
    'Cardiovascular': cardiovascular,
    'Glasgow_Coma_Scale': glasgow_coma_scale,
    'Creatinine': creatinine,
    'Mixed_NSCLC': mixed_nsclc,
    'Known_EGFR_ALK': known_egfr_alk,
    'Prior_Therapy_NSCLC': prior_therapy,
    'Tumor_Invading_Blood_Vessels': tumor_invading_blood_vessels,
    'Brain_Metastases': brain_metastases,
    'Other_Malignancies': other_malignancies,
    'Allergic_Reaction_to_Antibody_Therapy': allergic_reaction,
    'Significant_Intercurrent_Illness': intercurrent_illness,
    'Recent_Hemoptysis_or_Bleeding': recent_hemoptysis,
    'Major_Surgery_Past_28_Days': major_surgery
})