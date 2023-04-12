import json

id = input("Enter ID => ")
user = input("Enter Username => ")
passw = input("Enter Password => ")

data = {"id": id, "name": user, "pass": passw}

writ=open('./data/.www/user.json',"w+")
writ.write(json.dumps(data))
writ.close()
