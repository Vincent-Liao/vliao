from flask import Flask, request
from title_capture import main
import json
from random import randint
import os
app = Flask(__name__)


@app.route('/Title/Capture', methods=['Post'])
def title_capture():
    content = request.form['sources']
    print content
    tmp_name = str(randint(0, 999999)) + '.txt'
    tmp_file = open(tmp_name, 'w')
    tmp_file.write(content.encode('utf-8'))
    tmp_file.close()
    result = main(tmp_name)
    os.remove(tmp_name)
    print result
    return json.dumps(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)