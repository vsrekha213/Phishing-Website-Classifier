import pandas as pd

class Data_Getter:
    def __init__(self):
        self.train_file = r'C:\Users\Dell\ineuron\intern\Phishing Classifier\data_loading\InputFile.csv'

    def get_data(self):
        try:
            print("into data")
            self.data = pd.read_csv(self.train_file)
            return self.data

        except Exception as e:
            raise Exception()
