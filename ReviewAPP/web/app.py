from flask import Flask, request, render_template,json
app = Flask(__name__,template_folder="template") 


app = Flask(__name__)
app.debug = True

@app.route("/")
def Home():
   return render_template('main.html')
    
@app.route("/comment", methods=['POST'])
def comment():
        comment = request.form['Comment']
        if comment:
           print(request.form['Comment'])
           return comment    
        
        link = request.form['Link']
        if link:
           print(request.form['Link'])
           return link 
        
        
        
if __name__ == "__main__":
    app.run(port=8900)
