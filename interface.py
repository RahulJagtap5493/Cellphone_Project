from flask import Flask , jsonify,render_template,request,redirect,url_for
from utils import MobilePrice
import config

app = Flask(__name__)

@app.route("/")
def hello_flask():
    print("Welcome to Mobile price prediction")
    # return "hello"
    return render_template("index.html")

@app.route("/Mobile_price",methods = ["GET","POST"])

def predict():
    
    if request.method == "POST":
        print("We are in Post method")
        
        data = request.form
        print("Data :",data)
        
        weight       = request.form["weight"]
        resoloution  = eval(request.form["resoloution"])
        int_Memory   = request.form["int_Memory"]
        Ram          = request.form["Ram"]
        RearCam      = request.form["RearCam"]
        Front_Cam    = request.form["Front_Cam"]
        Battery      = request.form["Battery"]
        
        mobile_price = MobilePrice(data)
        price = mobile_price.get_pred_price()
        
        # return jsonify({"Price": price})
        return render_template("index.html",prediction = price)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=config.PORT_NUMBER)

        
        
