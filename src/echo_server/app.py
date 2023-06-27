from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_simple_geoip import SimpleGeoIP
from src.echo_server.libs.functions import get_env




app = Flask(__name__)
app.config.from_pyfile('config.py')
bootstrap = Bootstrap(app)
simple_ip = SimpleGeoIP(app)
ENV= get_env()

@app.route('/')
@app.route('/<user_input>')
@app.route('/index/<user_input>')
@app.route('/index.html/<user_input>')
def index(user_input='No Input Provided: please pass input via URL: \
            e.g http://URL-TO-ECHO-SERVER/USER-INPUT in your browser'):
    ip_data = simple_ip.get_geoip_data()
    return render_template('/index.html', title='P81', ip=ip_data['ip'],\
                        location=ip_data['location'], env=ENV, user_input=user_input)
