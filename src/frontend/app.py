from flask import Flask
import views
app = Flask(__name__)

app.run(port=5000)
