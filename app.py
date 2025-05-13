from flask import Flask, request, render_template, redirect, url_for, abort
import json

app = Flask(__name__)


# Load posts from posts.json
def load_posts():
    try:
        with open('posts.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []  # Return an empty list if the file doesn't exist


# Save posts to posts.json
def save_posts(posts):
    with open('posts.json', 'w') as f:
        json.dump(posts, f, indent=4)


@app.route('/')
def index():
    posts = load_posts()
    return render_template('index.html', posts=posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        author = request.form.get('author')
        title = request.form.get('title')
        content = request.form.get('content')

        posts = load_posts()

        next_id = max(post['id'] for post in posts) + 1 if posts else 1

        new_post = {
            'id': next_id,
            'author': author,
            'title': title,
            'content': content
        }

        posts.append(new_post)
        save_posts(posts)

        return redirect(url_for('index'))
    return render_template('add.html')


@app.route('/delete/<int:post_id>', methods=['POST'])
def delete(post_id):
    posts = load_posts()

    # Find the post with the given ID
    post_to_delete = next((post for post in posts if post['id'] == post_id), None)

    if post_to_delete:
        posts.remove(post_to_delete)
        save_posts(posts)
        return redirect(url_for('index'))
    else:
        abort(404)  # Handle the case where the post doesn't exist


def fetch_post_by_id(post_id):
    posts = load_posts()
    return next((post for post in posts if post['id'] == post_id), None)


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    post = fetch_post_by_id(post_id)
    if post is None:
        abort(404)

    if request.method == 'POST':
        post['author'] = request.form.get('author')
        post['title'] = request.form.get('title')
        post['content'] = request.form.get('content')
        save_posts(load_posts())  # Save the updated posts
        return redirect(url_for('index'))

    return render_template('update.html', post=post)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)