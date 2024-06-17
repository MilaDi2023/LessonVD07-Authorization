from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    password = 'supersecret'
    hashed = bcrypt.generate_password_hash(password).decode('utf-8')
    return f'Hashed password: {hashed}'

if __name__ == '__main__':
    app.run(debug=True)