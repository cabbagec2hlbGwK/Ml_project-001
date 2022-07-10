from bs4 import BeautifulSoup
import requests
from sqlalchemy import null
# print(data.title)
# print(len(data.tr.contents))
def extract(url, t):
    htmldata = requests.get(url=url)
    data = BeautifulSoup(htmldata.content, "html.parser")

    with open("full.txt",'a') as file:
        for a in data.findAll("tr"):
            formatnum = 0
            for td in a.findAll("td"):
                print(formatnum)
                if formatnum == 0:
                    formatnum = 1
                else:
                    file.writelines(', ')
                file.writelines(td.text.strip())
                print(td.text.strip())
                print("-"*30)

            file.writelines(f",{t}\n")
            print("*"*30)
def main():
    tim = ('midday','evening')
    t = 0
    for a in tim:
        t = t+1
        url = f"https://www.lotteryleaf.com/on/pick-2-{a}/"
        for year in range(12, 23):
            extract(f"{url}20{year}",t)

if __name__ == "__main__":
    main()

















