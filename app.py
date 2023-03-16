from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    text = request.args.get('button_text')
    print()
    print('Button Text:', text)
    print()
    return render_template('index.html')




if __name__ == '__main__':
    app.run(debug=True)
