from flask import Flask
from flask import render_template, url_for, flash, redirect, request, Response
  
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
    return render_template(r'home.html', data = instr)
  

if __name__ == '__main__':
    
    app.run()