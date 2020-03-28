from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World!"

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

if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port = 3000)
