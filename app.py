from flask import Flask
from flask import render_template, url_for, flash, redirect, request, Response
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import datetime
  
app = Flask(__name__)

cred = credentials.Certificate('servicekey.json')
firebase_admin.initialize_app(cred, {'databaseURL': "https://project-dmo-default-rtdb.asia-southeast1.firebasedatabase.app"})
  

@app.route('/')

def home():
    return render_template(r'home.html', title='Home')

@app.route('/handle_data', methods=['POST'])

def handle_data():
    instr = request.form['inp1']
    #print(instr)
    #instr += "joy"
    #print(instr)
    if(',' in instr):
        instr = instr.replace(" ", "")
    else:
        instr = instr.replace(" ", ",")
    
    today = datetime.now()
    today = str(today.strftime("%b-%d-%Y %H:%M:%S"))
    ref = db.reference('/')
    ref.child(today).set(instr)
    
    return render_template(r'home.html', data = instr)
  

if __name__ == '__main__':
    
    app.run()