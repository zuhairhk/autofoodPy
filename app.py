from flask import Flask, render_template, request
import locate

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def getvalue():
    data = request.form['query']

    rlist = locate.main(data)

    return render_template('passed.html', query = data, list = rlist)
    print(data)

if __name__ == '__main__':
    app.run(debug=True)