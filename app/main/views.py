from flask import render_template
from app.main import main



@main.route('/')
@main.route('/index')
def index():
    '''
    View function that displays home page
    '''
    title = 'HOME'
    return render_template('index.html', title=title)