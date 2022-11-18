import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.linear_model import LinearRegression
import pickle
from sklearn.svm import SVC, SVR 
from sklearn.model_selection import train_test_split

def pred(model,csvv):
    pass
    # d = pd.read_csv(csvv)
    # d['r1']=d['r1'].shift(-1)
    # print(d)
    # print(model.predict(d[:-1]))

def train(modelNmae,times):
    # get data
    data = pd.read_csv("data/data.csv")
    predict = 1
    modelNmae = f"model/{modelNmae}"
    x = data[:-predict]
    y = data["r1"].shift(-predict)[:-predict]
    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.1,)
    # traning and testing data
    max = 0
    try:
        classifer = pickle.load(open(modelNmae,'rb'))
        max = confidence = classifer.score(x_test, y_test)
    except:
        pass
    for num in range(times):
        x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.1,)
        #model traning
        classifer = SVR(kernel='rbf', C=1e3, gamma=.2)
        classifer.fit(x_train,y_train)
        # checking the model
        confidence = classifer.score(x_test, y_test)
        print(confidence)
        pred(classifer,"test.csv")
        if confidence > max:
            print("Saved")
            with open(modelNmae,'wb') as file:
                pickle.dump(classifer, file)
            max = confidence
        classifer = pickle.load(open(modelNmae,'rb'))
    return classifer

def getModel(name):
    classifer = pickle.load(open(name,'rb'))
    return classifer

def main():
    # # get data
    # data = pd.read_csv("data.csv")
    # predict = 10
    # x = data[:-predict]
    # y = data["r1"].shift(-predict)[:-predict]
    # x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.1,)
    # # traning and testing data
    model = train("long_run_1day.pickle",1000)

if __name__ == "__main__":
    main()