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
    if(',' in instr):
        instr = instr.replace(" ", "")
    if("  " in instr):
        instr = instr.replace("  "," ")
    instr = instr.replace(" ", ",")
    
    today = datetime.now()
    today = str(today.strftime("%b-%d-%Y %H:%M:%S"))
    conn = sqlite3.connect('logs.db')
    conn.execute("INSERT INTO LOGS (DATE,RESPONSE) VALUES (?, ?)",(today,instr,));
    conn.commit()
    conn.close()
    
    return render_template(r'home.html', data = instr)

@app.route('/logs', methods=['POST'])

def logs():
    conn = sqlite3.connect('logs.db')
    cursor = conn.execute("SELECT * from LOGS ORDER BY DATE DESC LIMIT 5")
    db_fetch_str = ""
    for row in cursor:
        db_fetch_str += str(row)
        db_fetch_str += "<br>"
    conn.commit()
    conn.close()
    return render_template(r'home.html', data1 = db_fetch_str, data2 = "Logs for 5 days:")
    

if __name__ == '__main__':
    
    app.run()