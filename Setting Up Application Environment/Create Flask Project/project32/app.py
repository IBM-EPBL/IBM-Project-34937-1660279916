from flask import Flask, jsonify, request,render_template
  
app = Flask(__name__)
  
  
@app.route('/hello', methods=['GET'])
def helloworld():
    if(request.method == 'GET'):
        data = {"data": "Hello World"}
        return render_template("index.html")
  
  
if __name__ == '__main__':
    app.run(debug=True)