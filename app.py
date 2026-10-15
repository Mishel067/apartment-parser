from flask import Flask
from flask import render_template
from parser import ToDataBase

app = Flask(__name__)
with ToDataBase('apartment.db') as db:
    apartments = db.get_all('apartment')
@app.route('/')
def index():
    with ToDataBase('apartment.db') as db:
        apartments = db.get_all('apartment')

    return render_template('index.html', apartments=apartments)

if __name__ == "__main__":
    app.run(debug=True)