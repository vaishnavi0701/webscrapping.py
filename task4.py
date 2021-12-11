import json
import requests
from bs4 import BeautifulSoup

def scrap_movie_details(link):
    # print(link)
    dic={}

    link_data=requests.get(link)
    # print(link_data)
    soup=BeautifulSoup(link_data.text,"html.parser")
    # print(soup)
    dic["name"]=soup.find("h1").text
    # print(dic["name"])
    
    movie_bio=soup.find("div",class_="movie_synopsis clamp clamp-6 js-clamp").get_text().strip()
    
    # print(bio)
    dic["Bio"]=movie_bio
    
    main = soup.find("div",class_="panel-body content_body")
    # print(main)
    sub=main.find("ul",class_="content-meta info")
    # print(sub)
    all=sub.find_all("li",class_="meta-row clearfix")
    # print(all)

    for i in all:
        dic[i.find("div",class_="meta-label subtle").text.strip()]=i.find("div",class_="meta-value").text.replace(" "," ").text.replace("\n","").strip()
    print(dic)
    with open ("task4.json","w") as f:
        json.dump(dic,f,indent=4)
    
scrap_movie_details("https://www.rottentomatoes.com/m/black_panther_2018")




