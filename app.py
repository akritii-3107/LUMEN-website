from flask import Flask,render_template

app=Flask(__name__)

base_url = "https://<your-username>.github.io/<your-repository-name>"

@app.route('/')
def index():
    home_url = f"{base_url}/"
    return render_template('index.html',about_url=home_url)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True,port=8000)

