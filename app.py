from flask import Flask, redirect, render_template,request,session, url_for
import sqlite3
app=Flask(__name__)

app.secret_key='dare to crack it,dare not to crack it'

@app.route('/',methods=['GET','POST'])
def home():
    session.clear()
    return render_template('home.html')


@app.route('/question1',methods=['POST','GET'])
def q1():
    if request.method=='POST':
        session['name']=request.form.get('name')
        conn=sqlite3.connect('q.db')
        c=conn.cursor()
        c.execute('select * from q_table')
        t=c.fetchall()
        for k,i in enumerate(t):
            print(i)
            session[f'a{k}']=i[-1]
            print(k,"#",i[-1])
        conn.close()
        
        return render_template('question1.html',t=t)
@app.route('/question2',methods=['POST'])
def q2():
    if request.method=='POST':
        if session['a0']==request.form.get('q1') and session['a1']==request.form.get('q2') and session['a2']==request.form.get('q3') and session['a3']==request.form.get('q4') and session['a4']==request.form.get('q5'):
            session['name']=request.form.get('name')
            conn=sqlite3.connect('q.db')
            c=conn.cursor()
            c.execute('select * from q_table')
            t=c.fetchall()
            conn.close()

            return render_template('question2.html',t=t)
        else:
            return render_template('sorry.html',t=f"Sorry {session['name']} you have not cleared Round 1")
@app.route('/result',methods=['POST'])
def result():
    if request.method=='POST':
        if session['a5']==request.form.get('q1') and session['a6']==request.form.get('q2') and session['a7']==request.form.get('q3') and session['a8']==request.form.get('q4') and session['a9']==request.form.get('q5'):
            return render_template('hurray.html')
@app.route('/timeout',methods=['POST','GET'])
def timeout():
    if request.method=='POST':
        redirect(url_for('home'))
        return render_template('sorry.html',t=f"Sorry {session['name']} time out you have not cleared this Round")
    else:
        return render_template('sorry.html',t=f"Sorry {session['name']} time out you have not cleared this Round")
if __name__=='__main__':
    app.run()