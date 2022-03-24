from flask import Flask,render_template
from flask_mysqldb import MySQL

app=Flask(__name__)

app.config['MYSQL_HOST']="remotemysql.com"
app.config['MYSQL_USER']="7uHI9MM9vC"
app.config['MYSQL_PASSWORD']="gUZhI4W7rX"
app.config['MYSQL_DB']="7uHI9MM9vC"
app.config['MYSQL_CURSORCLASS']="DictCursor"
mysql =MySQL(app)

#Loading Home Page
@app.route("/")
def home():
    con=mysql.connection.cursor()
    sql="SELECT * FROM form"
    con.execute(sql)
    res=con.fetchall()
    return render_template("home.html",datas=res)
    
if __name__=="__main__":
    app.run(debug=True)
    
