import os
import psycopg2
from flask import Flask
from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

conn = psycopg2.connect(
    host = 'localhost',
    database = 'bicycle'
)
cur = conn.cursor()

@app.route('/shop')
def login():
    return render_template('shop.html')

@app.route('/shop', methods = ['POST', 'GET'])
def buy():
    if request.method == 'POST':
        print(request.form['bike'])
        if request.form['bike'] == 'Buy Custom Bike #5':
            cur.execute('INSERT INTO bicycle (name, email, username, password, bicycle, price)'
                        'VALUES(%s, %s, %s, %s, %s, %s)',
                        ('test', 'test', 'test', 'test', 'bike1', 10))
        elif request.form['bike'] == 'bike2':
            cur.execute('INSERT INTO bicycle (name, email, username, password, bicycle, price)'
                        'VALUES(%s, %s, %s, %s, %s, %s)',
                        ('test', 'test', 'test', 'test', 'bike2', 20))
        elif request.form['bike'] == 'bike3':
            cur.execute('INSERT INTO bicycle (name, email, username, password, bicycle, price)'
                        'VALUES(%s, %s, %s, %s, %s, %s)',
                        ('test', 'test', 'test', 'test', 'bike3', 30))
        elif request.form['bike'] == 'bike4':
            cur.execute('INSERT INTO bicycle (name, email, username, password, bicycle, price)'
                        'VALUES(%s, %s, %s, %s, %s, %s)',
                        ('test', 'test', 'test', 'test', 'bike4', 40))
        elif request.form['bike'] == 'bike5':
            cur.execute('INSERT INTO bicycle (name, email, username, password, bicycle, price)'
                        'VALUES(%s, %s, %s, %s, %s, %s)',
                        ('test', 'test', 'test', 'test', 'bike5', 50))
        elif request.form['bike'] == 'bike6':
            cur.execute('INSERT INTO bicycle (name, email, username, password, bicycle, price)'
                        'VALUES(%s, %s, %s, %s, %s, %s)',
                        ('test', 'test', 'test', 'test', 'bike6', 60))
        elif request.form['bike'] == 'bike7':
            cur.execute('INSERT INTO bicycle (name, email, username, password, bicycle, price)'
                        'VALUES(%s, %s, %s, %s, %s, %s)',
                        ('test', 'test', 'test', 'test', 'bike7', 70))
        elif request.form['bike'] == 'bike8':
            cur.execute('INSERT INTO bicycle (name, email, username, password, bicycle, price)'
                        'VALUES(%s, %s, %s, %s, %s, %s)',
                        ('test', 'test', 'test', 'test', 'bike8', 80))
        elif request.form['bike'] == 'bike9':
            cur.execute('INSERT INTO bicycle (name, email, username, password, bicycle, price)'
                        'VALUES(%s, %s, %s, %s, %s, %s)',
                        ('test', 'test', 'test', 'test', 'bike9', 90))
        elif request.form['bike'] == 'bike10':
            cur.execute('INSERT INTO bicycle (name, email, username, password, bicycle, price)'
                        'VALUES(%s, %s, %s, %s, %s, %s)',
                        ('test', 'test', 'test', 'test', 'bike10', 100))
        else:
            cur.execute('INSERT INTO bicycle (name, email, username, password, bicycle, price)'
                        'VALUES(%s, %s, %s, %s, %s, %s)',
                        ('error', 'error', 'error', 'error', 'error', 0))

        conn.commit()
        cur.close()
        conn.close()
        return render_template('login.html')

if __name__ == '__main__':
    app.debug = True
    app.run(debug = True)