from flask import Flask, render_template
import pyjokes

app = Flask(__name__)

@app.route("/")
def index():
   joke = pyjokes.get_joke()
   return render_template("index.html", joke=joke)

if __name__ == "__main__":
   app.run(debug=True,port=5005)