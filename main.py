from flask_mysqldb import MySQL
from flask import Flask, render_template, redirect, request, url_for, session
import yaml

#init app
app = Flask(__name__)

#opening the yaml file contating the credentials
db = yaml.full_load(open('db.yaml'))

#calling database credentials 
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

#crearing a connection cursor
# cursor = mysql.connection.cursor()


@app.route("/", methods=['GET','POST'])
def index():
    return render_template("index.html", title="Homepage")

@app.route("/signup")
def signup():
    return render_template('signup.html', title="SignUp")


if __name__ == "__main__":
    app.run(debug=True)



