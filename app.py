from flask import Flask,request
app = Flask(__name__)
@app.route("/")
def calculator():
	return """
	<h1> My Docker Calculator </h1>
	<form action ="/calculate" method ="get">
	<input type = "number" name = "num1" placeholder = " First Number" required>
	<select name = "operation">
		<option value = "add"> + </option>
		<option value = "subtract"> - </option>
		<option value = "multiply"> * </option>
		<option value = "divide"> / </option>
	</select>
	<input type = "number" name = "num2" placeholder = "Second Number" required>
	<button type = "submit"> Calculate </button>
	</form>
	"""
@app.route("/calculate")
def calculate():
	num1 = float(request.args.get("num1"))
	num2 = float(request.args.get("num2"))
	operation = request.args.get("operation")

	if operation == "add":
		result = num1 + num2
	elif operation == "subtract":
		result = num1-num2
	elif operation == "multiply":
		result = num1*num2
	elif operation == "divide":
		if num2 ==0:
			return "Error: Can't divide by zero"
		result = num1/num2
	else:
		return "Invalid Operation"
	return f"<h1>Result = {result}</h1><a href = '/'> Back to Calculator </a>"
app.run(host="0.0.0.0", port = 5000)
