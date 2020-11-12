from flask import Flask,render_template, request, Markup
from flask_pymongo import PyMongo
from bson import ObjectId
import json 


import pymongo
app = Flask(__name__)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient.Patient

mycol = mydb.Doctor

#mongo = PyMongo(app)
#result=list(mycoltech.find({}))



	


@app.route("/",methods=['GET','POST'])
def start():
	
	if request.method == 'POST':
		pid = request.form['patientid']
		disease = request.form['disease']
		
		result=mycol.update({"PatientID":pid,"Result": ''},{'$set':{ "Result":disease}})
		return ("success")
		#if result:

			#mycol.save({"PatientID":pid,"Result":disease})
			#return ("success")
		#else:
		##	return ("Already updated")
	return render_template("index.html")

            
        

 	

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)


 







	