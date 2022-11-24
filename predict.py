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
    # d = d.drop(d[d['time '] == 2].index)
    # d.reset_index()
    # d = d.drop(columns="time ")
    d = d.sort_values(by=["year", "Mon", "date"])
    d.reset_index()
    print(d)
    return
    d['r1'] = d['r1'].shift(-1*pre)
    print("data")
    print(model.predict(d[:-1*pre]))


def main():
    pred("long_run_1day.pickle", "data/predict/data.csv", 1)


if __name__ == "__main__":
    main()
