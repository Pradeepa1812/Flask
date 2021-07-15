from flask import Flask,render_template,request,redirect
from flask_mysqldb import MySQL
import yaml


app=Flask(__name__)


#Configure db

db=yaml.load(open('db.yaml'))


app.config['MYSQL_HOST']=db['mysql_host']
app.config['MYSQL_USER']=db['mysql_user']
app.config['MYSQL_PASSWORD']=db['mysql_password']
app.config['MYSQL_DB']=db['mysql_db']

mysql=MySQL(app)

@app.route('/',methods=['GET','POST'])
def home():
    if request.method=="POST":
        name=request.form['name']
        email=request.form['email']

        cur =mysql.connection.cursor()
        cur.execute("Insert into users(name,email) values (%s, %s)",(name,email))
        mysql.connection.commit()
        cur.close()
        return redirect('/users')
    return render_template("validation.html")

@app.route('/users')
def users():
    cur=mysql.connection.cursor()
    resultvalue=cur.execute("select * from users")
    if resultvalue>0:
        userdetails=cur.fetchall()
        return render_template('users.html',userdetails=userdetails)

if __name__=='__main__':
    app.run(debug=True)