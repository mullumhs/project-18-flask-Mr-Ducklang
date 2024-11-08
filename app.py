from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

@app.route('/basic')
def basic():
    return render_template('basic.html')

@app.route('/greet/<name>')
def greet(name):
    return render_template('greet.html', name=name)



@app.route('/inventory')
def inventory():

    inventory_items = ['banana', 'cherry', '1990 Mazda MX-5','100,000kg of uranium', 'toothpaste', 'apple']

    return render_template('inventory.html', inventory=inventory_items)

@app.route('/test/<message>')

def test(message):

    return render_template('test.html', message=message)


@app.route('/profile/<username>')
def profile(username):
    return render_template('profile.html', username=username)

#GET Requests data from server and POST submits data to server
@app.route('/contact', methods=['GET', 'POST'])

def contact():
    #checks if method is post request
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Here you would typically save this data or send an email
        #after processing form data, redirects to thank you page here
        return redirect(url_for('thankyou', name=name, message=message))

    return render_template('contact.html')



@app.route('/thankyou')

def thankyou():

    name = request.args.get('name')

    message = request.args.get('message')

    return render_template('thankyou.html', name=name, message=message)


if __name__ == '__main__':
    app.run(debug=True)