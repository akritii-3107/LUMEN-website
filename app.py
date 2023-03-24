from flask import Flask,render_template,url_for

app=Flask(__name__)

base_url = "https://akritii-3107.github.io/LUMEN-website"

@app.route(base_url+'/')
def index():
    return render_template("index.html")

@app.route(base_url+'/about')
def about():
    return render_template('about.html')

@app.route(base_url+'/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True,port=8000)

