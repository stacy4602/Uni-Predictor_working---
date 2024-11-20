from flask import Flask,render_template,url_for,request,redirect
from flask import *

app= Flask(__name__)

import csv
  
with open('dept.csv', 'r') as read_obj:
    csv_reader = csv.reader(read_obj)
    temp = list(csv_reader)
    department = list()
    for i in temp:
        department.append(i[0])
 
with open('College-Name.csv', 'r') as read_obj_1:
    csv_reader_1 = csv.reader(read_obj_1)
    temp = list(csv_reader_1)
    Name = list()
    C_name = list()
    for i in temp:
        Name.append(i[0])
    for j in Name:
        n=j.split(',')[0]
        C_name.append(n)

with open('Colllege_Code.csv', 'r') as read_obj_2:
    csv_reader_2 = csv.reader(read_obj_2)
    temp = list(csv_reader_2)
    Code = list()
    for i in temp:
        Code.append(i[0])

with open('Course_code.csv', 'r') as read_obj_3:
    csv_reader_3 = csv.reader(read_obj_3)
    temp = list(csv_reader_3)
    Dept_code = list()
    for i in temp:
        Dept_code.append(i[0])

COMMUNITY = ["OC", "BC", "BCM", "MBC", "DNC", "SC", "SCA", "ST"]        

    
@app.route('/', methods = ["GET","POST"])
def predict():
    return render_template("index.html",percent=0,dept=department,College_name=C_name,College_code=Code,dept_code=Dept_code,com=COMMUNITY)    


@app.route('/result', methods = ["GET","POST"])
def result():
    return render_template("index.html" ,percent=76,dept=department,College_name=C_name,College_code=Code,dept_code=Dept_code,com=COMMUNITY)     

@app.route('/Landing', methods = ["GET","POST"])
def landing():
    return render_template("Landing Page.html")

@app.route('/collegeinfo', methods = ["GET","POST"])
def info():
    return render_template("/college_info/college.html")    


if __name__=='__main__':
    app.run(debug=True)

