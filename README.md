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

## Usage

To use the dataset, you can use the `RadiologyReportsDataset` class in `dataset.py`. Here is an example:

```python
from radset import RadiologyReportsDataset

dataset = RadiologyReportsDataset()
train_dataset, test_dataset = dataset.load_data()

# Show a sample from the train dataset
dataset.show_sample(train_dataset)

# Show a sample from the test dataset
dataset.show_sample(test_dataset)
```

This will load the data from the .csv files and print a sample from each dataset.
