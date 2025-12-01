from flask import Flask, jsonify

app = Flask(__name__)  # this starts your web app

@app.route('/hello/square/<int:num>')  # this defines a route: /hello
def square(num):
    return f"{num} squared is {num ** 2}"

if __name__ == '__main__':
    app.run(debug=True)

