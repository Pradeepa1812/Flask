from flask import Flask,redirect,url_for,render_template,request
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="Success"
    else:
        res="Fail"
    return "The person has  "+str(res)

@app.route('/fail/<int:score>')
def fail(score):
    return "The person has failed" +str(score)

@app.route('/results/<int:marks>')
def results(marks):
    result=""
    if marks<50:
        result="fail"
    else:
        result="success"
    return redirect(url_for(result,score=marks))

@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        ds=float(request.form['ds'])
        ml=float(request.form['ml'])
        dl=float(request.form['dl'])
        total_score=(ds+ml+dl)/3
        print(total_score)
    

    return redirect(url_for("success",score=total_score))

if __name__=='__main__':
    app.run(debug=True)