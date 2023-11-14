from flask import Flask, render_template
from excel import ExcelFile

excel_object = ExcelFile("cups.xlsx")
app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contacts/")
def contacts():
    return """<b> Тел.: </b> 23534534534 <br>
        <b>email:</b> codify@gmail.com"""

@app.route("/cups/")
def cups_list():
    cup_names = excel_object.get_cup_names()
    cup_names = cum_names.split("\n")
    return render_template("cum_list.html", cup_names=cup_names)

@app.route("/cup/<number>")
def cup_detail(number):
    cup_info, img_path = excel_object.get_cup_info(number)
    cup_info = cup_info.replace("\n", "<br>")
    return f"""{cup_info}
        <br>
        <img src='/static/{img_path}'/>
        """

app.run()