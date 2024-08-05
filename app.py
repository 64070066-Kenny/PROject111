import os
from flask import Flask, render_template

app = Flask(__name__, template_folder=".")

@app.route('/')
def home():
    # Use 'red' as the default color if APP_COLOR is not set
    env_var_colour = os.getenv('APP_COLOR', 'green')
    return render_template("index.html", color=env_var_colour)

@app.route('/<string:name>')
def template(name):
    return render_template("index.html", color=name)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8081)



    