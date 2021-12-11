import json

def get_lang_count():
    file=open("task5.json","r")
    var=json.load(file)
    # print(var)
    list=[]
    for i in var:
        # print(i)
        # print(i["Original Language"])
        if (i["Director:"] not in list):
            list.append(i["Director:"])
            # print(list)
    dict={}
    list1=[]
    for j in list:
        # print(j)
        i=0
        count=0
        while i<len(var):
            # print(i)
            if j==var[i]["Director:"]:
                count+=1
            i+=1
        dict.update({j:count})
        # print(dict)
    list1.append(dict)
    print(list1)
    with open("task7.json","w") as f:
        json.dump(list1,f,indent=4)

get_lang_count()

































































# a=["minakshi"]
# b=[]
# count=0
# for i in range(len(a)):
#     print(a[i])
#     for j in range (len(a[i])):
#         # count+=1
#         if i==0:
#             b.append(a[i][j])
#     print(b,":",count)
    # i=0
    # while x <= b:
# i=0
# d=[]
# for i in a:
#     if i in a:
#         d.append(i)
#     print(d[i])

