#!/venvs/py27flask-env/bin/python
from flask import Flask, redirect, render_template, request
app = Flask(__name__)

femtoDB = {} 
#ultra light in-memory db substitute for preliminary dev't!
#(single user system reduces overhead until we want to add more users)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def index_receiver():
    add_fields = ['users_name', 'city', 'moreinfo']
    for af in add_fields:
        femtoDB[af] = request.form[af]
    return redirect("/result/")


@app.route('/result/')
def getResult():
    return render_template('resultspage.html',
                            users_name = femtoDB['users_name'],
                            city = femtoDB['city'],
                            moreinfo = femtoDB['moreinfo'],
                            )    
    


if __name__ == '__main__':
  app.run(port=8000, debug=True)
 