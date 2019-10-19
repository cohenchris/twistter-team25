from flask import Flask, url_for, redirect, render_template


app = Flask(__name__)


@app.route("/")
def display_home_page():
	return render_template('sample.html', **locals())


if __name__ == '__main__':
	app.run(debug=True)