from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

DATA_FILE = 'posts.json'

def load_posts():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_posts(posts):
    with open(DATA_FILE, 'w') as f:
        json.dump(posts, f, indent=4)

def get_post_by_id(post_id):
    posts = load_posts()
    for post in posts:
        if post['id'] == post_id:
            return post
    return None

@app.route('/')
def index():
    posts = load_posts()
    return render_template('index.html', posts=posts)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        posts = load_posts()
        new_id = max([post['id'] for post in posts], default=0) + 1
        new_post = {
            'id': new_id,
            'author': request.form['author'],
            'title': request.form['title'],
            'content': request.form['content']
        }
        posts.append(new_post)
        save_posts(posts)
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/delete/<int:post_id>')
def delete(post_id):
    posts = load_posts()
    posts = [post for post in posts if post['id'] != post_id]
    save_posts(posts)
    return redirect(url_for('index'))

@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    posts = load_posts()
    post = get_post_by_id(post_id)
    if not post:
        return "Post not found", 404
    if request.method == 'POST':
        post['author'] = request.form['author']
        post['title'] = request.form['title']
        post['content'] = request.form['content']
        save_posts(posts)
        return redirect(url_for('index'))
    return render_template('update.html', post=post)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
