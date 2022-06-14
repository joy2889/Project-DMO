from flask import Flask
from flask import render_template, url_for, flash, redirect, request, Response
from datetime import datetime
import sqlite3

  
app = Flask(__name__)


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
    conn = sqlite3.connect('logs.db')
    conn.execute("INSERT INTO LOGS (DATE,RESPONSE) VALUES (?, ?)",(today,instr,));
    conn.commit()
    conn.close()
    
    return render_template(r'home.html', data = instr)
  

if __name__ == '__main__':
    
    app.run()