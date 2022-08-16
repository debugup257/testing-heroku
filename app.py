from flask import Flask,render_template
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(
   database="d67fsm4svq5gp3", user='cthlqzrfduldux', password='284d42f2d7277cf2318c7053bb11f6665c3ba385f1abc9ca3668af049a5eb06e', host='ec2-44-195-100-240.compute-1.amazonaws.com', port= '5432'
)
c = conn.cursor()

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
