import pandas as pd
def headRemov():
    with open("results.txt",'r') as data:
        with open("finalcsv",'w') as file:
            for line in data.readlines():
                if "Date" not in line:
                    file.writelines(line)

def stripString():
    months = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}
    data = pd.read_csv("finalcsv.csv") 
    a =  data[['Date', 'year', 'win','time']]
    with open('data.csv','w') as file:
        file.writelines("month,year,result,time \n")
        for i in a.itertuples():
            x,y= i.Date.split(' ')
            line = f"{months[x]},{y.strip()},{i.year},{i.win.replace(' ','')},{i.time}\n"
            file.writelines(line)



if __name__=='__main__':
    stripString()