from flask import Flask, render_template, request, jsonify
from time import time
import json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.is_json:
        if request.method == 'GET':
            seconds = time()
            return jsonify({'seconds': seconds})

        if request.method == 'POST':
            card_text = json.loads(request.data).get('text')  # .form or .json
            new_text = f'I got: {card_text}'
            return jsonify(({'data': new_text}))

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
