"""Main application entry point."""

from flask import Flask, render_template
from loguru import logger

from src.config.settings import TEMPLATE_DIR, STATIC_URL, STATIC_ROOT
from src.utils.logger import setup_logger

# Initialize logger
setup_logger()

# Create Flask app
app = Flask(__name__, 
           template_folder=str(TEMPLATE_DIR),
           static_url_path=STATIC_URL,
           static_folder=str(STATIC_ROOT))

@app.route('/')
def index():
    """Render the index page."""
    return render_template('base.html')

def main():
    """Run the application."""
    try:
        logger.info('Starting application...')
        app.run(debug=True)
    except Exception as e:
        logger.error(f'Application failed to start: {e}')
        raise

if __name__ == '__main__':
    main() 