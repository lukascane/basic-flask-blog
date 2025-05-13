# 1. Create the Route and Function
git add app.py
git commit -m "Feat: Add /add route and function for new blog posts"

# 2. Create the Form
git add templates/add.html
git commit -m "Feat: Create add.html form template"

# 3. Handle POST Requests
git add app.py
git commit -m "Feat: Handle POST requests in /add route"

# 4. Link from Home Page
git add templates/index.html
git commit -m "Feat: Add link to /add route from home page"

# 5. Push Changes
git push origin main
 Git Commits
The following Git commits were used to implement the add and delete functionalities:

Option 1: Separate Commits for Each Feature

Commit 1: Adding the /add route

Feat: Add /add route for creating new blog posts

This commit introduces the /add route, which allows users to create new blog posts.
-   Handles both GET (displaying the form) and POST (processing form submission) requests.
-   Implements form data handling using request.form.get().
-   Generates unique post IDs.
-   Adds new posts to the posts.json file.
-   Redirects to the index page after successful post creation.

Commit 2: Adding the /delete route

Feat: Add /delete route for deleting blog posts

This commit introduces the /delete/<post_id> route, which allows users to delete existing blog posts.
-   Handles POST requests to delete posts.
-   Identifies the post to delete using the provided post_id.
-   Removes the post from the posts.json file.
-   Redirects to the index page after successful deletion.
-   Implements error handling for non-existent post IDs using abort(404).

Option 2: Combined Commit

If you made all the changes in one go, you can combine them into a single commit:

Feat: Implement add and delete functionality for blog posts

This commit adds the ability to create and delete blog posts.

-   Introduces the /add route:
    -   Handles both GET (displaying the form) and POST (processing form submission) requests.
    -   Implements form data handling using request.form.get().
    -   Generates unique post IDs.
    -   Adds new posts to the posts.json file.
    -   Redirects to the index page after successful post creation.
-   Introduces the /delete/<post_id> route:
    -   Handles POST requests to delete posts.
    -   Identifies the post to delete using the provided post_id.
    -   Removes the post from the posts.json file.
    -   Redirects to the index page after successful deletion.
    -   Implements error handling for non-existent post IDs using abort(404).

How to Run the Application
Clone the repository.

Set up a virtual environment.

Install the required packages (Flask).

Run the app.py file.

Access the application in your web browser. 

**1. Update the Index Template (`index.html`)**

* Modify your `index.html` template to include an "Update" button within each blog post's display. This button should link to the `/update/<post_id>` route, where `<post_id>` is the unique ID of the blog post.

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>My Flask Blog</title>
        <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
    </head>
    <body>
        <header>
            <h1>Welcome to My Flask Blog!</h1>
            <nav>
                <ul>
                    <li><a href="{{ url_for('index') }}">Home</a></li>
                    <li><a href="{{ url_for('add') }}">Add New Post</a></li>
                </ul>
            </nav>
        </header>
        <main>
            {% for post in posts %}
            <article class="post">
                <h2>{{ post.title }}</h2>
                <p><em>Written by {{ post.author }}</em></p>
                <p>{{ post.content }}</p>
                <a href="{{ url_for('update', post_id=post.id) }}">Update</a>
                <form action="{{ url_for('delete', post_id=post.id) }}" method="post">
                    <input type="submit" value="Delete">
                </form>
            </article>
            {% endfor %}
        </main>
    </body>
    </html>
    ```
* **Explanation:**
    * An update button is added, which is an anchor tag (`<a>`) that sends a GET request to the  `/update/<post_id>`  route.

**2.  Add the Update Route (`app.py`)**

* Add the following code to your  `app.py`  file to define the  `/update/<post_id>`  route and handle the updating of blog posts:

    ```python
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
            abort(404)  #  Handle the case where the post doesn't exist
            
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
    ```
* **Explanation:**
    * The  `@app.route('/update/<int:post_id>', methods=['GET', 'POST'])`  decorator defines a route that accepts both GET and POST requests and takes an integer  `post_id`  from the URL.
    * The  `update()`  function first calls  `fetch_post_by_id()`  to retrieve the post.
    * If the post doesn't exist, it returns a 404 error using  `abort(404)`.
    * If the request method is POST, it updates the post's author, title, and content using data from the form and then saves the updated data to  `posts.json`  using  `save_posts()`.  It then redirects the user to the index page.
    * If the request method is GET, it renders the  `update.html`  template, passing the  `post`  data so the form can be pre-filled with the existing values.
    * The  `fetch_post_by_id`  function is added to retrieve a post by its ID.

**3.  Create the Update Form (`update.html`)**

* Create a new HTML file named  `update.html`  in your  `templates`  folder. This file will contain the form for users to edit their blog post details.

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Edit Post</title>
        <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
    </head>
    <body>
        <h1>Edit Blog Post</h1>
        <form action="{{ url_for('update', post_id=post.id) }}" method="post">
            <label for="author">Author:</label><br>
            <input type="text" id="author" name="author" value="{{ post.author }}" required><br><br>
    
            <label for="title">Title:</label><br>
            <input type="text" id="title" name="title" value="{{ post.title }}" required><br><br>
    
            <label for="content">Content:</label><br>
            <textarea id="content" name="content" rows="4" required>{{ post.content }}</textarea><br><br>
    
            <input type="submit" value="Update Post">
        </form>
        <a href="{{ url_for('index') }}">Back to Home</a>
    </body>
    </html>
    ```
* **Explanation:**

    * The  `action`  attribute of the form is set to  `{{ url_for('update', post_id=post.id) }}`  to ensure the form submits the data to the correct URL.
    * The  `value`  attribute of the input fields is set to  `{{ post.author }}`,  `{{ post.title }}`, and  `{{ post.content }}`  respectively. This pre-fills the form with the existing post data.