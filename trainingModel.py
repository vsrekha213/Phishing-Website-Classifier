#from sklearn.model_selction import train_testsplit
from data_preprocessing import preprocess
import pickle

#from data_preprocessing import clustering
from sklearn.model_selection import train_test_split
from model_prediction import prediction
from data_loading import data_loader
from best_model_finder import tuner

class trainModel():
    def trainingModel(self):
        try:
            #data loading
            #print('into trina model')
            data_getter = data_loader.Data_Getter()
            data = data_getter.get_data()
            #print("after data fetch")

            #data preprocessing
            #print("into dta preprocess")
            preprocessing = preprocess.Preprocessor()
            print("btw data preprocess")
            #data = preprocessor.replaceInvalidwithNull()
            #print("after dta preprocess")
            """
            is_null_present,cols_with_missing_values = preprocessor.is_null_present(data)

            if(is_null_present):
                data = preprocessor.impute_missing_values(data,cols_with_missing_values)
            """
           # print(data['Result'])
            print("into data split")
            X, Y = preprocessing.separate_label_feature(data,'Result')
            print("b/w split")
            x_train, x_test, y_train, y_test = train_test_split(X,Y, test_size=1 / 3,random_state=36)
            print("COMPLETED")
            model_finder =  tuner.Model_Finder()

            best_model_name, best_model = model_finder.get_best_model(x_train, y_train, x_test, y_test)
            print("sucess!! into prediction")
            prediction_model = prediction.Prediction()
            filename = 'finalized_model.sav'
            pickle.dump(best_model, open(filename, 'wb'))

            prediction_model.pred_model(best_model,x_train, x_test, y_train, y_test)



            #print("after tuning returns")
            #print('************BEST MODEL *********** {0} \n Model PARAMS **********************{1}'.format(best_model_name,best_model))




        except Exception as e:

            raise Exception()







