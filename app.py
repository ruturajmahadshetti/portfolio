from flask import Flask,render_template
import pandas as pd

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/publications')
def publications():
    df = pd.read_csv('./publications.csv')
    journal_pubs = df['journal'].dropna().tolist()
    conf_pubs = df['conference'].dropna().tolist()
    return render_template('pub.html', journals=journal_pubs, conferences=conf_pubs)
    return render_template('pub.html')

@app.route('/projects')
def projects():
    return render_template('proj.html')
@app.route('/contact')
def contact():
    return render_template("contact_info.html")
if __name__=="__main__":
    app.run(debug=True)

