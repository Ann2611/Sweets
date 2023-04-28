from flask import Flask
app=Flask(__name__)
@app.route("/")
def pageHome():
  an=12
  return an
print("Ann")
app.run(host='0.0.0.0',debug=True)