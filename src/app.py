
import pyjokes
import logging
from waitress import serve
from flask import Flask, render_template, request


# Initialize Flask app
app = Flask(__name__)

# Configure logging with datetime
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)


@app.route("/")
def index():
    try:
        # Get the selected language from the query parameter, default to 'en' (English)
        lang = request.args.get('lang', 'en')

        # Validate the language option
        if lang not in ['en', 'de', 'es']:
            lang = 'en'
            logger.warning("Invalid language selection. Defaulting to 'en'.")

        # Get the joke in the selected language
        joke = pyjokes.get_joke(language=lang)
        logger.info(f"Joke fetched successfully in language: {lang}")
        return render_template(
            "index.html",
            joke=joke,
            selected_lang=lang
        )

    except Exception as e:
        logger.error(f"Error fetching joke: {e}")
        return render_template(
            "index.html",
            joke="Sorry, something went wrong.",
            selected_lang='en'
        )


if __name__ == "__main__":
    # Production server setup
    serve(app, host='0.0.0.0', port=5000)
