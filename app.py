from flask import Flask, request, render_template, redirect, url_for
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
        # Get data from the form
        author = request.form.get('author')
        title = request.form.get('title')
        content = request.form.get('content')

        # Load existing posts
        posts = load_posts()

        # Generate a unique ID (Improved)
        if posts:
            next_id = max(post['id'] for post in posts) + 1
        else:
            next_id = 1

        # Create the new post
        new_post = {
            'id': next_id,
            'author': author,
            'title': title,
            'content': content
        }

        # Add the new post to the list
        posts.append(new_post)

        # Save the updated posts list
        save_posts(posts)

        # Redirect to the index page
        return redirect(url_for('index'))
    else:
        # Render the form for adding a new post
        return render_template('add.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
