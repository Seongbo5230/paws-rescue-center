"""Flask Application for Paws Rescue Center."""
from flask import Flask, render_template
app = Flask(__name__)

"""Information regarding the Pets in the System."""
# id, name, age, bio
# dictionary
pets = [
            {"id": 1, "name": "Nelly", "age": "5 weeks", "bio": "I am a tiny kitten rescued by the good people at Paws Rescue Center. I love squeaky toys and cuddles."},
            {"id": 2, "name": "Yuki", "age": "8 months", "bio": "I am a handsome gentle-cat. I like to dress up in bow ties."},
            {"id": 3, "name": "Basker", "age": "1 year", "bio": "I love barking. But, I love my friends more."},
            {"id": 4, "name": "Mr. Furrkins", "age": "5 years", "bio": "Probably napping."}, 
        ]

@app.route("/")
def homepage():
    """View function for Home Page."""
    return render_template("5_home.html", pets=pets)


@app.route("/about")
def about():
    """View function for About Page."""
    return render_template("5_about.html")



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)



# from flask import Flask, render_template
# app = Flask(__name__)

# @app.route("/")
# def home():
#     Users = {
#                 "Archie":"Amsterdam", 
#                 "Veronica":"London", 
#                 "Betty":"San Francisco", 
#                 "Jughead":"Los Angeles"
#             }
#     return render_template("5_index.html", users=Users)

# @app.route("/about")
# def about():
#     Users = {
#                 "Archie":"Amsterdam", 
#                 "Veronica":"London", 
#                 "Betty":"San Francisco", 
#                 "Jughead":"Los Angeles"
#             }
#     return render_template("5_index.html", users=Users)


# if __name__ == "__main__":
#     app.run(debug=True, host="0.0.0.0", port=3000)
