from flask import Flask, render_template


app = Flask(__name__)

@app.route('/basic')
def basic():
    return render_template('basic.html')

@app.route('/greet/<name>')
def greet(name):
    return render_template('greet.html', name=name)

@app.route('/inventory')

def inventory():

    inventory_items = ['banana', 'cherry', '1990 Mazda MX-5','100,000kg of uranium', 'toothpaste']

    return render_template('inventory.html', inventory=inventory_items)

if __name__ == '__main__':
    app.run(debug=True)