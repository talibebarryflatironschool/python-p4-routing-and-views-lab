#!/usr/bin/env python3

# from flask import Flask
# #!/usr/bin/env python3

#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    # Returns an H1 element with the title of the application.
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:text>')
def print_string(text):
    # Print the provided text to the console and display it.
    print(text)
    return text

@app.route('/count/<int:number>')
def count(number):
    # Display all numbers from 0 to number-1, each on a new line.
    # A newline character is added at the end of the output to match the test.
    return "\n".join(str(i) for i in range(number)) + "\n"

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    # Perform the specified math operation.
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation.lower() == 'div':
        if num2 == 0:
            result = 'Error: Division by zero'
        else:
            result = num1 / num2
    elif operation == '%':
        if num2 == 0:
            result = 'Error: Division by zero'
        else:
            result = num1 % num2
    else:
        result = 'Invalid operation'
    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
