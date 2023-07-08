from flask import Flask, request
print("__name__", __name__)
app = Flask(__name__)
@app.route("/")
def welcome():
    return 'Welcome to Flask '
@app.route("/greetinperson/<string:name>")
def personalizedgreeting(name):
    return f"{name} Greetings from Flask"
@app.route("/add/<int:num1>/<int:num2>")
def add(num1,num2):
    return f"The result of addition is {str(num1+num2)}"
@app.route("/users/add",methods=["post"])
def addUser():
    user = request.get_json()
    print("Post Method")
    return user

if(__name__ == "__main__"):
    app.run(debug=True)