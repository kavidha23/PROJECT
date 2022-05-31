# coding: utf-8

from flask import Flask, jsonify, request
from pymongo import MongoClient
from flask_cors import CORS, cross_origin
client = MongoClient('mongodb://localhost:27017/kavidha')
db = client['kavidha']

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/users', methods=['POST', 'GET'])
def data():
    
    if request.method == 'POST':
        body = request.json
        firstName = body['firstName']
        lastName = body['lastName']
        emailId = body['emailId']
        department = body['department']
        gender = body['gender']
        salary = body['salary']
        country = body['country']
    
        db['users'].insert_one({
            "firstName": firstName,
            "lastName": lastName,
            "emailId": emailId,
            "department" : department,
            "gender" : gender,
            "salary" : salary,
            "country" : country
        })
        return jsonify({
            'status': '200. Data is posted to MongoDB',
            'firstName': firstName,
            'lastName': lastName,
            'emailId': emailId,
            "department" : department,
            "gender" : gender,
            "salary" : salary,
            "country" : country
        })
    
 
    if request.method == 'GET':
        allData = db['users'].find()
        dataJson = []
        for data in allData:
            id = data['_id']
            firstName = data['firstName']
            lastName = data['lastName']
            emailId = data['emailId'],
            department = data['department'],
            gender = data['gender'],
            salary = data['salary']
            country = data['country']
            
            dataDict = {
                'id': str(id),
                'firstName': firstName,
                'lastName': lastName,
                'emailId': emailId,
                "department" : department,
                "gender" : gender,
                "salary" : salary,
                "country" : country
            }
            
            dataJson.append(dataDict)
        print(dataJson)
        return jsonify(dataJson)
if __name__ == '__main__':
    app.run()




