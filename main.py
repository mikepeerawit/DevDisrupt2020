from flask import Flask
from flask import jsonify
from flask import request
from pymongo import MongoClient


app = Flask(__name__)
file = open('train.csv')
maxSeat = 70
data = []
for line in file:
    trainNumber,takenSeat = line.split(',')
    availableSeat = maxSeat - int(takenSeat)
    data.append({'trainNumber':trainNumber, 'takenSeat':int(takenSeat), 'availableSeat':int(availableSeat)})

@app.route('/')
def home():
    return "<h1> Data Collecting from Train </h1>"

@app.route('/insertdata')
def insertdata():
    client=MongoClient("mongodb+srv://usertest:VTAFqNqnUk5nF8EL@cluster0.jodck.mongodb.net/?retryWrites=true&w=majority")
    db=client.Train
    db.Train_status.insert_many(data)
    return '<h1> Finished </h1>'

@app.route('/findscore')
def findscore():
    client=MongoClient("mongodb+srv://usertest:VTAFqNqnUk5nF8EL@cluster0.jodck.mongodb.net/?retryWrites=true&w=majority")
    db=client.Train
    trainNumber = request.args.get('trainNumber')
    data = db.Train_status.find()
    ret = dict()
    for value in data:
        if(value['trainNumber'] == trainNumber):
            ret['trainNumber'] = {'trainNumber':value['trainNumber'], 'takenSeat':value['takenSeat'], 'availableSeat': value['availableSeat']}
    return jsonify(ret)

if __name__ == '__main__':
    app.run()
