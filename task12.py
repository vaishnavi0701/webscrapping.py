



# from bs4 import BeautifulSoup
# import json
# import requests
# import pprint
# from task1 import task1data
# data=task1data

# def main_fun(data):
    
#     def scrap_movie_cast(link,movie_name):
#         d1={}
#         link_data=requests.get(link)
#         soup=BeautifulSoup(link_data.text,'html.parser')
#         d1["Name"]=movie_name
#         table=soup.find('div',class_='castSection')
#         celebrity_link=table.find_all('a',class_="unstyled articleLink")
#         # print(celebrity_link) 
#         celebrity_name=table.find_all('span',class_='characters subtle smaller')
#         # print(celebrity_name)
#         # a_tag=table.find_all('a')
#         d1={}
#         d2={}
#         dic={}
#         for i in range(len(celebrity_link)):
            
            
#             Name=celebrity_name[i]['title']
#             # print(Name)
#             # if i==0:

#             link=+celebrity_link[i]['href']

#             cast_id=""
#             id=len(link)-1

#             while id>=0:
#                 if link[id]!="/":
#                     cast_id+=link[id]
#                 else:
#                     break
#                 id=id-1
#             cast_id=list(cast_id)
#             cast_id.reverse()
#             cast_id=''.join(cast_id)
#             # print(cast_id)
#             d1[cast_id]=Name 
#             # print(d1)

#         dic[movie_name]=d1
#         return dic

#     movie_cast_list=[]
#     for i in data:
#             for j in i:
#                 movie_name=i["movieName"]
#                 if j=="movie_link":
#                     # print( i[j])
#                     movie_details_dic=scrap_movie_cast(i[j],movie_name) 
#                     movie_cast_list.append(movie_details_dic)
#                     # movie_filename=str(movie_filename(movie_name))
#                 with open("task12.json","w") as f:
#                     json.dump(movie_cast_list,f,indent=3)
#     # print(movie_cast_list)

# data5=main_fun(data)





from bs4 import BeautifulSoup
import json
import requests
import pprint

def movie_cast(movie_url):
    list=[]
    data=requests.get(movie_url)
    soup=BeautifulSoup(data.text,"html.parser")
    main=soup.find_all("div",class_="panel-body content_body")
    # print(main[1])
    sec=main[1].find("div",class_="castSection")
    all=sec.find_all("div",class_="cast-item")
    for i in all:
        list.append(i.find("span")["title"])
    # return list

    with open("task12.json","w") as file:
        json.dump(list,file,indent=4)

    return list
    

pprint.pprint(movie_cast("https://www.rottentomatoes.com/m/black_panther_2018"))





