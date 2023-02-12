# Flask modules
from flask   import render_template, request
from jinja2  import TemplateNotFound
from .extensions import login_required

# App modules
from app import app

@app.route('/', methods=['GET'])
# @login_required
def index():
    try:        
        return render_template( 'home/index.html' )    
    except TemplateNotFound:
        return render_template('home/page-404.html'), 404


@app.route('/login', methods=['GET','POST'])
def login():
    try:
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']
        return render_template( 'home/sign-in.html' )    
    except TemplateNotFound:
        return render_template('home/page-404.html'), 404
    



@app.route('/sign-up', methods=['GET'])
def signup():
    try:        
        return render_template( 'home/sign-up.html' )    
    except TemplateNotFound:
        return render_template('home/page-404.html'), 404


@app.route('/tables', methods=['GET'])
def tables():
    try:        
        return render_template( 'home/tables.html' )    
    except TemplateNotFound:
        return render_template('home/page-404.html'), 404