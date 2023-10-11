from flask import render_template
from . import about  # Import the Blueprint

@about.route('/about')
def about_us():
    """
    Render the about template on the / route
    """
    return render_template('about/about_us.html')
