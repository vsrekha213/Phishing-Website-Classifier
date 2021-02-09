
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics  import roc_auc_score,accuracy_score
from sklearn.model_selection import GridSearchCV
from xgboost import XGBClassifier

class Model_Finder:


    def __init__(self):
        self.clf = RandomForestClassifier()
        self.xgb = XGBClassifier(objective='binary:logistic')

    def get_best_params_for_random_forest(self,train_x,train_y):


        try:
            print("***************RF***************")

           self.param_grid = {"n_estimators": [10, 50, 100, 130], "criterion": ['gini', 'entropy'],
                        "max_depth": range(2, 4, 1), "max_features": ['auto', 'log2']}
    #        self.param_grid = {"n_estimators": [10], "criterion": ['gini'],
     #                       "max_depth": [4], "max_features": ["log2"]}


            self.grid = GridSearchCV(estimator=self.clf, param_grid=self.param_grid, cv=5)

            self.grid.fit(train_x, train_y)


            self.criterion = self.grid.best_params_['criterion']
            self.max_depth = self.grid.best_params_['max_depth']
            self.max_features = self.grid.best_params_['max_features']
            self.n_estimators = self.grid.best_params_['n_estimators']

            self.clf = RandomForestClassifier(n_estimators=self.n_estimators, criterion=self.criterion,
                                              max_depth=self.max_depth, max_features=self.max_features)

            self.clf.fit(train_x, train_y)


            return self.clf
        except Exception as e:
            print(e)
            raise Exception()

    def get_best_params_for_xgboost(self,train_x,train_y):
        print("************xgb***************")



        try:
            self.param_grid_xgboost = {

               'learning_rate': [0.5, 0.1, 0.01, 0.001],
               'max_depth': [3, 5, 10, 20],
               'n_estimators': [10, 50, 100, 200]
               #'learning_rate': [0.001],
               #'max_depth': [5],
              #'n_estimators': [100]

            }

            self.grid= GridSearchCV(XGBClassifier(objective='binary:logistic'),self.param_grid_xgboost,cv=5)

            self.grid.fit(train_x, train_y)


            self.learning_rate = self.grid.best_params_['learning_rate']
            self.max_depth = self.grid.best_params_['max_depth']
            self.n_estimators = self.grid.best_params_['n_estimators']

            self.xgb = XGBClassifier(learning_rate=1, max_depth=5, n_estimators=50)
            self.xgb.fit(train_x, train_y)

            return self.xgb
        except Exception as e:
            print(e)
            raise Exception()


    def get_best_model(self,train_x,train_y,test_x,test_y):

        try:
            print("*************xgb check****************")
            self.xgboost= self.get_best_params_for_xgboost(train_x,train_y)
            self.prediction_xgboost = self.xgboost.predict(test_x)

            if len(test_y.unique()) == 1:
                self.xgboost_score = accuracy_score(test_y, self.prediction_xgboost)

            else:
                self.xgboost_score = roc_auc_score(test_y, self.prediction_xgboost)

            print("*************RF check****************")
            self.random_forest=self.get_best_params_for_random_forest(train_x,train_y)
            self.prediction_random_forest=self.random_forest.predict(test_x)

            if len(test_y.unique()) == 1:
                self.random_forest_score = accuracy_score(test_y,self.prediction_random_forest)

            else:
                self.random_forest_score = roc_auc_score(test_y, self.prediction_random_forest)

            if(self.random_forest_score <  self.xgboost_score):
                return 'XGBoost',self.xgboost
            else:
                return 'RandomForest',self.random_forest

        except Exception as e:
            print(e)

