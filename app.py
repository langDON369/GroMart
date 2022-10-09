from flask import Flask,render_template,request
import pickle
import numpy as np

popular_df = pickle.load(open('popular_.pkl','rb'))
pt = pickle.load(open('pt.pkl','rb'))
items = pickle.load(open('item.pkl','rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                           product = list(popular_df['Title'].values),
                           cat=list(popular_df['category'].values),
                           image=list(popular_df['image'].values),
                           rating=list(popular_df['avg_ratings'].values)
                           )

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

@app.route('/recommend',methods=['post'])
def recommend():
    user_input = request.form.get('user_input')
    index = np.where(pt.index == user_input)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:5]

    data = []
    for i in similar_items:
        item = []
        temp_df = items[items['Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Title')['Title'].values))
        item.extend(list(temp_df.drop_duplicates('Title')['category'].values))
        item.extend(list(temp_df.drop_duplicates('Title')['image'].values))
        data.append(item)

    print(data)

    return render_template('recommend.html',data=data)

if __name__ == '__main__':
    app.run(debug=True)
