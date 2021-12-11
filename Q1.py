import json

office_time=input("enter the office time : ")
meetings=int(input("enter  how many meetings you want"))

i=1
mylist=[]

while i<=meetings:
        submission_info=input("entre the submission date YYYY-MM-DD ,Time HH:MM:SS and employeeid :")
        meeting_info=input("enter the meeting date YYYY-MM-DD,Time HH:MM,meeting duration in hrs : ")
        submission=submission_info.split()
        meeting=meeting_info.split()
        mydic={}
        mydic["Employee Id"]=submission[2]
        mydic["submission_date"]=submission[0]
        mydic["submission_time"]=submission[1]
        mydic["meeting_date"]=meeting[0]
        mydic["meeting_start_time"]=meeting[1]
        time=meeting[1].split(':')
        end_time=int(time[0])+int(meeting[2])
        end_time1=str(end_time)+":"+time[1]
        mydic["meeting_end_time"]=end_time1
        mylist.append(mydic)
        i=i+1
# print(i)
print(mylist)  

for i in mylist:
        end=i["meeting_end_time"].split(":")
        start=i["meeting_start_time"].split(":")
        if int(end[0])>17.30:
            mylist.remove(i)
for k in mylist:
    count=0
    for j in mylist:
        if k["submission_time"]==j["submission_time"]:
            count+=1
            if count>1:
                mylist.remove(k)

with open("aai.json","w")as file:
        data=json.dump(mylist,file,indent=4)

print(mylist)
