from flask import Flask, render_template
import socket
import mysql.connector
import os

app = Flask(__name__)

DB_Host = os.environ.get('DB_Host') or "localhost"
DB_Database = os.environ.get('DB_Database') or "mysql"
DB_User = os.environ.get('DB_User') or "root"
DB_Password = os.environ.get('DB_Password') or "paswrd"

@app.route("/")
def main():
    db_connect_result = False
    err_message = ""
    try:
        # Establishing the connection and storing it in a variable
        conn = mysql.connector.connect(host=DB_Host, database=DB_Database, user=DB_User, password=DB_Password)
        color = '#39b54b'
        db_connect_result = True
        # Close the connection after successful use
        conn.close()
    except mysql.connector.Error as e:
        color = '#ff3f3f'
        err_message = str(e)

    return render_template('hello.html', debug=f"Environment Variables: DB_Host={DB_Host}; DB_Database={DB_Database}; DB_User={DB_User}; DB_Password={DB_Password}; {err_message}", db_connect_result=db_connect_result, name=socket.gethostname(), color=color)

@app.route("/debug")
def debug():
    color = '#2196f3'
    return render_template('hello.html', debug=f"Environment Variables: DB_Host={DB_Host}; DB_Database={DB_Database}; DB_User={DB_User}; DB_Password={DB_Password}", color=color)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
