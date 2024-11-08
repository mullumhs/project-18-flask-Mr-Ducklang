from flask import Flask, redirect

app = Flask(__name__)



# Our "database" is just a list

todos = ["clean", "dinosaur", "car",]


@app.route('/')
def list_todos():
    # use a loop and <br> to join all to-do's into one string
    # return the to-do list as one string
    task = ''
    for chore in todos:
        task += (f"{chore}<br>")
    return task



@app.route('/add/<task>')

def add_todo(task):
    # append the 'task' to the list
    todos.append(task)
    # Return back to the to-do list page
    return redirect('/')


@app.route('/delete/<int:task_id>')

def delete_todo(task_id):
    # delete the item at the specified position in the list
    todos.pop(task_id)

    # Return back to the to-do list page
    return redirect('/')



if __name__ == '__main__':

    app.run(debug=True)