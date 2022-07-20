def pred(classifier, csvv):
    modelPath = f'model/{classifier}'
    try:
        model = pickle.load(open(modelPath, 'rb'))
        max = model.score(x_test, y_test)
    except:
        pass
    d = pd.read_csv(csvv)
    d['r1'] = d['r1'].shift(-1)
    print(d)
    print(model.predict(d[:-1])


def main():
    model=train("long_run_1day.pickle", 1000)
    pred(cla)


if __name__ == "__main__":
    main()
