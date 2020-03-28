from flask import Flask

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

@app.route("/")
def home():
    return "Paws Rescue Center 🐾"

@app.route("/about")
def about():
    return "We are a non-profit organization working as an animal rescue. We aim to help you connect with the purrfect furbaby for you! The animals you find on our website are rescued and rehabilitated animals. Our mission is to promote the ideology \"adopt, don\'t hop\"! "

if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port = 3000)
