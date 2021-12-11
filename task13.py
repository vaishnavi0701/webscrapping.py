from task5 import t5
import pprint
import os
from bs4 import BeautifulSoup
import json
import requests
from task9 import url_list

def task13(url_list):
    if os.path.exists("/home/vinaata/Desktop/vaishnavi_webscrapping/task13.json")==True:
        with open("/home/vinaata/Desktop/vaishnavi_webscrapping/task12.json","r")as file:
            data=file.read()
            t13=json.loads(data)
        return t13
    else:
        final=[]
        cast_list=[]
        for k in range(len(url_list)):
            x=requests.get(url_list[k])
            soup=BeautifulSoup(x.text,"html.parser")
            main=soup.find("div",class_="castSection")
            all=main.find_all("div",class_="cast-item")
            for i in all:
                cast_list.append(i.find("span")["title"])
            t5[k]["cast"]=cast_list
            final.append(t5[k])
            print(final)
            break



