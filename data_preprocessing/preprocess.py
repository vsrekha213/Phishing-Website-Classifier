import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer
from sklearn_pandas import CategoricalImputer




class Preprocessor:



    def remove_columns(self,data,columns):

        self.data=data
        self.columns=columns
        try:
            self.useful_data=self.data.drop(labels=self.columns, axis=1) # drop the labels specified in the columns

            return self.useful_data
        except Exception as e:

            raise Exception()

    def separate_label_feature(self, data, label_column_name):

        try:
            self.X=data.drop(labels=label_column_name,axis=1)
            self.Y=data[label_column_name] # Filter the Label columns
            return self.X,self.Y
        except Exception as e:

            raise Exception()

    def dropUnnecessaryColumns(self,data,columnNameList):

        data = data.drop(columnNameList,axis=1)
        return data


    def replaceInvalidValuesWithNull(self,data):



        for column in data.columns:
            count = data[column][data[column] == '?'].count()
            if count != 0:
                data[column] = data[column].replace('?', np.nan)
        return data

    def is_null_present(self,data):

        self.null_present = False
        self.cols_with_missing_values=[]
        self.cols = data.columns
        try:
            self.null_counts=data.isna().sum()
            for i in range(len(self.null_counts)):
                if self.null_counts[i]>0:
                    self.null_present=True
                    self.cols_with_missing_values.append(self.cols[i])
            if(self.null_present):
                self.dataframe_with_null = pd.DataFrame()
                self.dataframe_with_null['columns'] = data.columns
                self.dataframe_with_null['missing values count'] = np.asarray(data.isna().sum())
                self.dataframe_with_null.to_csv('preprocessing_data/null_values.csv')

            return self.null_present, self.cols_with_missing_values
        except Exception as e:

            raise Exception()

    def encodeCategoricalValues(self,data):

     data["class"] = data["class"].map({'p': 1, 'e': 2})

     for column in data.drop(['class'],axis=1).columns:
            data = pd.get_dummies(data, columns=[column])

     return data


    def encodeCategoricalValuesPrediction(self,data):



        for column in data.columns:
            data = pd.get_dummies(data, columns=[column])

        return data


