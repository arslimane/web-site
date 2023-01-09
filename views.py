from flask import Blueprint,render_template,request
from running_model import predict,pre1,lemx,p
import asyncio
views=Blueprint(__name__,"views")
@views.route("/")
def index():
    return render_template("index.html")



@views.route("/submit",methods=['POST'])
def get_text():
    text=request.form["text"]
    text=pre1(text)
    result=predict(text)
    return render_template("index.html",result=result,text=request.form["text"])




