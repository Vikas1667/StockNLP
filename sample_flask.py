from flask import Flask, Response
app = Flask(__name__)

@app.route("/")
def hello():
    return '''
        <html>
          <body>
            <a href="/get_csv">Click me.</a>
          </body>
        </html>
      '''

@app.route("/get_csv")
def get_csv():
    csv = '1,2,3\n4,5,6\n'
    return Response(
        csv,
        mimetype="text/csv",
        headers={"Content-disposition":
                 "attachment; filename=myplot.csv"})


app.run(debug=True)