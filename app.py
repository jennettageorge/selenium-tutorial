
#!/usr/bin/env python3

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return app.send_static_file('greet.html')


@app.route("/greet")
def greet():
    username = request.args.get('name')
    return render_template('index.html', name=username)


if __name__ == "__main__":
    app.run()
