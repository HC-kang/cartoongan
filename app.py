from flask import Flask, request, jsonify
from werkzeug.serving import WSGIRequestHandler
from cartoongan import cartoongan

app = Flask(__name__)

@app.route('/image/convert_cartoon', methods=['POST'])
def convert_catrtoon():
    data = request.get_json()

    if 'image' not in data:
        return '', 400
    
    cartoon_img_data = cartoongan.convert(data['image'])

    return "", 200

@app.route('/')
def index():
    return "<h1>Welcome to cartoongan server </h1>"

if __name__ == '__main__':
    WSGIRequestHandler.protocol_version = 'HTTP/1.1'
    app.run(host='0.0.0.0', port = 5000)