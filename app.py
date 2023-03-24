from flask import Flask,render_template,url_for

app=Flask(__name__)

base_url = "https://akritii-3107.github.io/LUMEN-website"

@app.route('/')
def index():
    index_url = url_for("index", _external=True)
    return render_template("index.html", index_url=index_url, base_url=base_url)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True,port=8000)

