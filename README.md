# Radiology Reports Dataset Repository

This project is a dataset repository for radiology reports. The dataset consists of labeled parts of the text in radiology reports that we want to detect. The repository is similar to the Huggingface dataset and can be used with the `load_dataset` function.

## Installation

To install the required libraries, run the following command:

```
pip install -r requirements.txt
```

## Dataset

The dataset is divided into a training set and a testing set. Each set is stored in a .csv file with the following columns:

- `report_id`: A unique identifier for each report.
- `report_text`: The text of the radiology report.
- `labeled_text`: The part of the text that we want to detect.

Here is an example of the data in the training set:

| report_id | report_text | labeled_text |
|-----------|-------------|--------------|
| 1 | Patient presents with a fracture in the left radius. Recommend immediate cast. | fracture in the left radius |
| 2 | No visible issues in the patient's chest x-ray. Heart and lungs appear normal. | No visible issues |
| 3 | Signs of pneumonia in the right lung. Patient should be started on antibiotics. | Signs of pneumonia in the right lung |
| 4 | Patient's MRI shows a possible tumor in the brain. Recommend further testing. | possible tumor in the brain |
| 5 | No abnormalities detected in the patient's abdominal ultrasound. | No abnormalities detected |

## Usage

To use the dataset, you can use the `RadiologyReportsDataset` class in `dataset.py`. Here is an example:

```python
from dataset import RadiologyReportsDataset

dataset = RadiologyReportsDataset()
train_dataset, test_dataset = dataset.load_data()

# Show a sample from the train dataset
dataset.show_sample(train_dataset)

# Show a sample from the test dataset
dataset.show_sample(test_dataset)
```

This will load the data from the .csv files and print a sample from each dataset.
