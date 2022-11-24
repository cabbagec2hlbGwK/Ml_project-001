import pandas as pd


def headRemov():
    with open("data/dump/full.txt", 'r') as data:
        with open("data/dump/final.csv", 'w') as file:
            for line in data.readlines():
                if "Date" not in line:
                    file.writelines(line)


def addHead():
    with open("data/dump/final.csv", 'r') as f:
        content = f.read()
        with open("data/dump/finalH.csv", 'w') as f2:
            f2.writelines('Date,year,win,price,time\n')
            f2.write(content)


def stripString():
    months = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
              'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
    data = pd.read_csv("data/dump/finalH.csv")
    a = data[['Date', 'year', 'win', 'price', 'time']]
    with open('data/predict/data.csv', 'w') as file:
        file.writelines("Mon,date,year,r1,time \n")
        for i in a.itertuples():
            x, y = i.Date.split(' ')
            line = f"{months[x]},{y.strip()},{i.year},{i.win.replace(' ','')},{i.time}\n"
            file.writelines(line)


if __name__ == '__main__':
    headRemov()
    addHead()
    stripString()
