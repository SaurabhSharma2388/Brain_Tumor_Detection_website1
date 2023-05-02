from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
  return render_template('home.html')

@app.route("/execute_python_function", methods=["POST"])
def execute_python_function():
  # Get the uploaded file
  file = request.files['image']
  
  result = "File uploaded successfully!"
  return result

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)