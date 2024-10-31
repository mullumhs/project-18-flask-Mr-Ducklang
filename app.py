from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/hello/<name>')
def say_hello(name):
    return f"G'day {name}!"

@app.route('/calc/<int:num1>/<string:operation>/<int:num2>')
def calculator(num1, operation, num2):

    # Program the logic of a calculator here
    # E.g. if operation = "add" then result = num1 + num2

    if operation == "add":
        result = num1 + num2
        return f'{num1} plus {num2} equals {result}'

    elif operation == "min":
        result = num1 - num2
        return f'{num1} minus {num2} equals {result}'

    elif operation == "mul":
        result = num1*num2
        return f'{num1} multiplied by {num2} equals {result}'

    elif operation == "div":
        result = num1/num2
        return f'{num1} divided by {num2} equals {result}'

    else:
        print("Error, invalid operation")
        return()
    
@app.route('/search')

def search():

    query = request.args.get('q', '')

    category = request.args.get('category', 'all')

    return f'Searching for "{query}" in category: {category}'

    





if __name__ == '__main__':
    app.run(debug=True)