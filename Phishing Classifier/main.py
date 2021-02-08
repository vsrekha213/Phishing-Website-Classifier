from model_prediction import prediction
from trainingModel import trainModel

class Train:
    def trainRoute():
        try:
            #print("enter train")
            train_modelobj = trainModel()
            #print("into train")
            t1, t2 = train_modelobj.trainingModel()
            #print("after train")
            #print(t1,t2)

            #if request.json['folderPath'] is not None:
             #   path = request.json['folderPath']



        except Exception as ex:
            print(ex)



if __name__ == "__main__":
    print("enter")
    train = Train
    train.trainRoute()



