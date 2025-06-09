from app import create_app
from flask_cors import CORS

app = create_app()

# 启用 CORS
CORS(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9000, debug=True)