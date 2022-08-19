from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template,request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///Giftcard.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Picsifid(db.Model):
    Sno = db.Column(db.Integer, primary_key=True)
    Address = db.Column(db.String(500), nullable=False)
    Name = db.Column(db.String(200), nullable=False)
    OrderNo = db.Column(db.Integer)
    Subject = db.Column(db.String(500), nullable=False)
    Message = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.Address} - {self.Name}"


@app.route("/", methods=["GET","POST"])
def hello_world():
    if request.method =="POST":
        EmailAddress = request.form["Email Address"]
        Name = request.form["Name"]
        OrderNo = request.form["Order No"]
        Subject = request.form["Subject"]
        Message = request.form["Message"]
        data = Picsifid(Address = EmailAddress, Name = Name,OrderNo = OrderNo, Subject = Subject, Message = Message )
        db.session.add(data)
        db.session.commit()
    return render_template('Giftcard.html')




if __name__=="__main__":
    app.run(debug=True)
