from flask import Flask, render_template, request
import pyjokes

app = Flask(__name__)

@app.route("/")
def index():
    # Get the selected language from the query parameter, default to 'en' (English)
    lang = request.args.get('lang', 'en')
    
    # Validate the language option
    if lang not in ['en', 'de', 'es']:
        lang = 'en'
    
    # Get the joke in the selected language
    joke = pyjokes.get_joke(language=lang)
    return render_template("index.html", joke=joke, selected_lang=lang)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
