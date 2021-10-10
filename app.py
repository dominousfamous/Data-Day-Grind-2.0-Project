from flask import Flask
from views import views

#Configure flask app
app = Flask(__name__)

#Register Blueprint
app.register_blueprint(views)

#Run app
if __name__ == "__app__":
    app.run(debug=True)

