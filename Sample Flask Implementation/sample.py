from flask import Flask,render_template

app=Flask(__name__)


fruit=[
    {
    'name':'Apple',
    'color':'red',
    'contains':'vitamins,minerals'
    },
    {
    'name':'Orange',
    'color':'org',
    'contains':'weightloss'
    }
]


@app.route('/')
def home():
    return render_template('base.html',title='Home',posts=fruit)





if __name__=='__main__':
      app.run(debug=True)