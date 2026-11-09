from flask import Flask
import json
import datetime
import os

app = Flask(__name__)

# Get the absolute path of the directory where backend.py is located
basedir = os.path.abspath(os.path.dirname(__file__))

@app.route('/news.all.get')
def get_news_all_articles():
    json_path = os.path.join(basedir, 'news_data.json')
    try:
        with open(json_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except Exception as e:
        data = {"error": str(e)}
    return json.dumps(data)

@app.route('/news.categories.get')
def get_news_categories():
    time_now_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = {
        'title': 'List of Categories',
        'time': time_now_str,
        'categories': [
            {'id': 1, 'name': 'Sports'},
            {'id': 2, 'name': 'Politics'},
            {'id': 3, 'name': 'Education'}
        ]
    }
    return json.dumps(data)

@app.route('/')
def index():
    return 'Welcome ENSIA Students from Flask!'

if __name__ == "__main__":
    app.run(port=8080)
