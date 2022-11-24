import pickle
import pandas as pd
def pred(classifier, csvv, pre):
    modelPath = f'model/{classifier}'
    try:
        model = pickle.load(open(modelPath, 'rb'))
        max = model.score(x_test, y_test)
    except:
        pass
    d = pd.read_csv(csvv)
    d['r1'] = d['r1'].shift(-1*pre)
    print(d)
    print("data")
    print(model.predict(d[:-1*pre]))


def main():
    pred("long_run_1day.pickle","data/data.csv", 5)


if __name__ == "__main__":
    main()
