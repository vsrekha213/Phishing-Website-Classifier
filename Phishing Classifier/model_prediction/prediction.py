from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
from sklearn.metrics import classification_report

class Prediction:

    def pred_model(self,best_model,x_train, x_test, y_train, y_test):
        #print(best_model)

        self.model = best_model
        self.model.fit(x_train,y_train)
        self.pred = self.model.predict(x_test)
        print(accuracy_score(self.pred,y_test))
        print(confusion_matrix(y_test, self.pred))
        print(classification_report(y_test, self.pred))




