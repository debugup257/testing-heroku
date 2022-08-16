from flask import Flask,render_template
import psycopg2

app = Flask(__name__)

# conn = psycopg2.connect(
#    database="zsykrjpg", user='zsykrjpg', password='hTl4Mjgl4Wl0QOmHLragl010RLsgN0eb', host='tiny.db.elephantsql.com', port= '5432'
# )
# c = conn.cursor()

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
