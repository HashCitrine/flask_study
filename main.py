from flask_cors import CORS

from config import init_flask

app = init_flask()
CORS(app)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5555)



