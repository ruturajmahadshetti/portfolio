from flask import Flask,render_template
import pandas as pd
import os
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/publications')
def publications():
    j_df = pd.read_csv('./docs/journal.csv')
    c_df = pd.read_csv('./docs/conference.csv')
    journal_pubs = j_df.to_dict(orient='records')
    conf_pubs = c_df['paper'].dropna().to_list()
    return render_template('pub.html', journals=journal_pubs, conferences=conf_pubs)
    return render_template('pub.html')

@app.route('/projects')
def projects():
    return render_template('proj.html')
@app.route('/contact')
def contact():
    return render_template("contact_info.html")
if __name__=="__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
