from flask import Flask, render_template, jsonify
# import the Flask class from flask module
# render_template to return html pages from function and pass some data to html pages for dyanamic infornmation

# then create an app object of type('Flask')
app = Flask(__name__)
# __name__ has initial value = __main__
data = [
  'Vihan', 'Kapoor', 'Payal', 'Kapoor', "Sanjay", "Kapoor", "Manju", "Kapoor"
]
# store some data in form of list or list of dictionary for accessing inside another function


# set the route of the app
@app.route("/")  #@ is decorator function
# below the route you have to define a function for returning a webpage on some request
def func():
  return render_template(
    'home.html', data=data
  )  #just below the route wrote the corresponding function            lhs data is the variable that will be passed into the html file for direct access


@app.route("/api/user_info")
def fun1():
  return jsonify(data)
  # jsonify is used for converting data into json


# for sending data in form of data variable we use this format

# way to run a flask program
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
