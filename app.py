from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/locations')
def locations():
    return render_template('locations.html')
    
@app.route('/ship_it')
def ship_it():
    return render_template('ship_it.html')
    

@app.route('/articles')
def articles():
    return render_template('articles.html')

@app.route('/support')
def support():
    return render_template('support.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
    
@app.route('/accepted_medicines')
def accepted_medicines():
    return render_template('accepted_medicines.html')
    
    
if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

if __name__ == '__main__':
    app.run(debug=True)


