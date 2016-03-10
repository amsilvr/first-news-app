from flask import Flask
from flask import render_template
app = Flask(__name__) #note double underscores

@app.route("/")
def index():
    template = 'index.html'
    return render_template(template)

if __name__ == '__main__':
    #fire up the flask test server
    app.run(debug=True, use_reloader=True)
    