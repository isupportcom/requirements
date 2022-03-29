import json
from flask import Flask,request
from flask_cors import CORS

import requests 
token = "N0Fh3HYzQ28OT0CT1Ka6BgMQg7Zro6Zl0HWHYL1r8CxabUbMV72TjkcPdXX"
app = Flask(__name__)
CORS(app)

api = "https://pca.oncloud.gr/s1services"



@app.route("/",methods=["GET"])

def main():
    if(token == request.args.get('token')):

        username = request.args.get('username')
        password = request.args.get('password')
        #print(username,password)
        #print('Mphke')
        data={
            'service':"login",
            'username':"Sparke",
            'password':"1234",
            'appId':"3001"
        }

        datas = json.dumps(data)
        r=requests.post(api,data=datas)
        #print(r.text)
        clientID = json.loads(r.text)
        objs = json.loads(r.text)
    # print(objs['objs'])
        company =json.loads(json.dumps(objs['objs']))
        #print(company[0]['COMPANY'])

    # print(r.text)
        data={
            "service": "authenticate",
            "clientID": clientID['clientID'],
            "company": company[0]['COMPANY'],
            "branch": company[0]['BRANCH'],
            "module": company[0]['MODULE'],
            "refid": company[0]['REFID'] 
        }
        datas = json.dumps(data)
    # print(datas)
        r=requests.post(api,data=datas)   
        clientID = json.loads(r.text)
       # print(r.text)

        data = { 
            'service':"SqlData",
            'clientID': clientID['clientID'],
            'appId':"3001",
            'SqlName':"AFM-KOD",
            "param1":username,
            "param2":password
        }
        datas= json.dumps(data)
        r = requests.post(api,data=datas)
        #print(r.text)
        return r.text 
    else:
        return "Require Token"
   
if __name__ == '__main__':
    app.run(debug=True,host="localhost",port="4000")