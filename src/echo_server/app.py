from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_simple_geoip import SimpleGeoIP
from src.echo_server.libs.functions import get_ip, get_location, get_env




app = Flask(__name__)
app.config.from_pyfile('config.py')
bootstrap = Bootstrap(app)
simple_ip = SimpleGeoIP(app)

@app.route('/')
@app.route('/<input>')
@app.route('/index/<input>')
@app.route('/index.html/<input>')
def index(input='No Input Provided: please pass input via URL: e.g http://URL-TO-ECHO-SERVER/USER-INPUT in your browser'):
    # ip = get_ip()
    # location = get_location()
    ip_data = simple_ip.get_geoip_data()
    if len(input):
        return render_template('/index.html', title='P81', ip=ip_data['ip'],location=ip_data['location'], input=str.capitalize(input)  )
    else:
        return render_template('/index.html', title='P81', ip=ip_data['ip'],location=ip_data['location'], input=str.capitalize(input))





