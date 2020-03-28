from flask import Flask, render_template

app = Flask(__name__)

@app.route("/educative")
def learn():
    return "Educate Page..."

@app.route("/<my_name>")
def greetings(my_name):
    return "Hello, I am " + my_name + "!"

@app.route("/square/<int:number>")
def show_square(number):
    """View that shows the square of the number passed by URL"""
    return "Square of " + str(number) + " is: " + str(number * number)

@app.route("/about")
def about():
    return render_template("about.html")

# # HTML
# @app.route("/")
# def home():
#     return "<h1>Welcome to the home page...</h1>"

# Flask framework looks for the HTML template files in the /templates directory
@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port = 3000)
