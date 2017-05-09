from flask import Flask, request
from title_capture import main
import json

app = Flask(__name__)


@app.route('/Title/Capture', methods=['Get'])
def title_capture():
    auth = request.args.get('authentication', '')
    if auth == '200':
        print '200'
        file_path = request.args.get('filepath', '')
        result = main(file_path)
    return json.dumps(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)