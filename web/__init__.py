from flask  import  *
from flask_socketio import  *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'glno$enac2020!'
socket = SocketIO(app, cors_allowed_origins='*')

@app.route('/')
def index():
    return render_template('index.html')

