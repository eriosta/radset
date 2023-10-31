import csv
from datasets import load_dataset

class RadiologyReportsDataset:
    def __init__(self, train_file='train.csv', test_file='test.csv'):
        self.train_file = train_file
        self.test_file = test_file

    def load_data(self):
        train_dataset = load_dataset('csv', data_files=self.train_file)
        test_dataset = load_dataset('csv', data_files=self.test_file)
        return train_dataset, test_dataset

    def show_sample(self, dataset, num_samples=1):
        for i in range(num_samples):
            print(dataset[i])

if __name__ == "__main__":
    dataset = RadiologyReportsDataset()
    train_dataset, test_dataset = dataset.load_data()
    print("Showing a sample from the train dataset:")
    dataset.show_sample(train_dataset)
    print("\nShowing a sample from the test dataset:")
    dataset.show_sample(test_dataset)