import pandas


df = pandas.read_csv('data.csv')
sorted_df = df.sort_values(['year','Mon','date']).reset_index()
print(sorted_df)
sorted_df.to_csv("data1.csv")