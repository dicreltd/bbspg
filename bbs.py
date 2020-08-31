from flask import *
from toukou import Toukou,ToukouDB

app = Flask(__name__)

@app.route('/')
def index():
    db = ToukouDB()
    toukous = db.get_all()
    db.close()
    return render_template("bbs.html",toukous=toukous)

@app.route('/',methods=['POST'])
def write():
    name = request.form['name']
    body = request.form['body']
    toukou = Toukou(0,name,body,None)

    db = ToukouDB()
    db.insert(toukou)
    db.close()
    #return render_template("write.html",toukou=toukou)
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=False)
