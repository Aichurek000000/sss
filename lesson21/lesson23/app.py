from flask import Flask
app = Flask(__name__)
@app.route("/about/")
def about():
    return "This site is for selling <b> cups </b>"
@app.route("/")
def homepage():
    return 'Hello world!'
@app.route("/home/")
def home():
    return '<a href="https://www.youtube.com/watch?v=Bmqpa-q08-o">click here!</a>'
#@app.route("/cup/<number>")
# def cup_detail(number):
    #cum_info, img_path = excel_object.get_cup_info(number)
    #cup_info = cu,_info.replace("\n", "<br>")
#return f {cup_info}
#<br>
#<img src = '/static/{img_path}'/>


app.run()