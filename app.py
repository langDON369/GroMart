from flask import Flask,render_template,request
import pickle
import numpy as np

popular_df = pickle.load(open('popular.pkl','rb'))
##pt = pickle.load(open('pt.pkl','rb'))
##books = pickle.load(open('books.pkl','rb'))
##similarity_scores = pickle.load(open('similarity_scores.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                           Item = list(popular_df['Title'].values),
                           des=list(popular_df['category'].values),
                           image=list(popular_df['image'].values),
                           ##votes=list(popular_df['num_ratings'].values),
                           rating=list(popular_df['avg_ratings'].values)
                           )
if __name__ == '__main__':
    app.run(debug=True)
