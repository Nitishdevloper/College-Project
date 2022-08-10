
# from flask import Flask, jsonify, request,render_template,session,redirect ,url_for
# # # from flask_mysqldb import MySQL
# # import MySQLdb.cursors
# import re
# from flaskext.mysql import MySQL
# import pymysql
  
# app = Flask(__name__)
# app.config.from_pyfile('config.py')
# mysql=MySQL()

# mysql.init_app(app)
# conn=mysql.connect()
# cursor=conn.cursor(pymysql.cursors.DictCursor)
  
# @app.route('/')
# def home():
#     return render_template('hk.html') 


# @app.route('/')
# def helloworld():
#     return render_template('Signin.html') 



# # @app.route('/hk')
# # def hk():
# #     return render_template('hk.html')



# # @app.route('/login',methods=['POST'])
# # def login() :

# #     if request.method=='POST':
# #         email=request.form['email']
# #         psw=request.form['psw']
# #         cursor.execute('SELECT * FROM signup WHERE email=%s AND psw=%s ',(email,psw))
# #         return render_template('Signin.html')
# #         # query1= query.fetchone()  
# #     return render_template("hk.html")  


# @app.route('/register',methods=['POST']) 
# def register():

#     if request.method=='POST':
#         name=request.form['name']
#         mob=request.form['mob']
#         email=request.form['email']
#         # psw=request.form['psw']
#         # mark=request.form['mark']
  
#         cursor.execute( 'INSERT INTO signup (name, mob, email ) VALUES (%s,%s,%s) ',
#         (name, mob, email))
#         conn.commit()
#         return redirect('login')

#     return render_template('login.html') 

# app.run(debug=True)

# ----------------------------------------------------------------------
from flask import Flask, render_template, request, redirect, url_for, flash
from flaskext.mysql import MySQL
import pymysql
 
app = Flask(__name__)
app.secret_key = "Cairocoders-Ednalan"
  
mysql = MySQL()
   
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'log'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
#   ================================================================
# @app.route('/')
# def demo():
#     return render_template('register.html')
# @app.route('/nkb', methods=['POST','GET'])
# def nkb():
#     conn = mysql.connect()
#     cur = conn.cursor(pymysql.cursors.DictCursor)
#     if request.method == 'POST':
#         fullname = request.form['fullname']
#         phone = request.form['phone']
#         email = request.form['email']
#         cur.execute("INSERT INTO signup (name, email, phone) VALUES (%s,%s,%s)", (fullname, email, phone))
#         conn.commit()
#         return redirect('login')
#     flash('Employee Added successfully')
        
#  =======================================================
@app.route('/')
def demo():
    return render_template('sign.html')
# @app.route('/Signin')
# def Signin():
#     return render_template('Signin.html')
 
# @app.route('/xyz', methods=['POST','GET'])
# def xyz():
#     conn = mysql.connect()
#     cur = conn.cursor(pymysql.cursors.DictCursor)
#     if request.method == 'POST':
#         fullname = request.form['fullname']
#         phone = request.form['phone']
#         email = request.form['email']
#         # bdy = request.form['bdy']
#         # gender = request.form['gender']
#         cur.execute("INSERT INTO nitish (name, email, phone) VALUES (%s,%s,%s)", (fullname, email, phone))
#         conn.commit()
#         return redirect('login')
#         flash('Employee Added successfully')
        
    
app.run(debug=True,port=7000)