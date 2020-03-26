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

if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port = 3000)
