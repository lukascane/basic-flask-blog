# 📝 Basic Flask Blog (JSON-based)

This is a simple blog application built using [Flask](https://flask.palletsprojects.com/) where users can **create**, **read**, **update**, and **delete** (CRUD) blog posts. All data is stored in a local `posts.json` file instead of a database, making it ideal for learning and lightweight deployments.

---

## 🚀 Features

- ✅ View all blog posts
- ➕ Add new posts
- 📝 Update existing posts
- ❌ Delete posts
- 🧠 Posts stored persistently in a `JSON` file

---

## 🛠️ Technologies Used

- Python 3.x
- Flask
- JSON for data persistence
- HTML/CSS (Jinja2 templating)

---

## 📁 Project Structure


basic-flask-blog/
├── app.py # Main Flask application
├── posts.json # Data storage for blog posts
├── templates/ # HTML templates
│ ├── index.html # Home page showing all posts
│ ├── add.html # Form to add new post
│ └── update.html # Form to update post
└── static/
└── style.css # Basic styling

yaml
Copy


---

## ⚙️ Setup Instructions

1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/basic-flask-blog.git
cd basic-flask-blog



---

## ⚙️ Setup Instructions

1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/basic-flask-blog.git
cd basic-flask-blog
Install Flask

bash
Copy
pip install flask
Run the App

bash
Copy
python app.py
Visit in Browser

arduino
Copy
http://localhost:5000/
🔍 Step-by-Step Functionality and Task Solving
1. Display Posts (Read)
File: index.html, app.py

Load posts from posts.json

Render them in a loop using Jinja2 in index.html

python
Copy
@app.route('/')
def index():
    posts = load_posts()
    return render_template('index.html', posts=posts)
2. Add New Post (Create)
File: add.html, app.py

Form to input author, title, and content

On POST, save data to posts.json with a new ID

python
Copy
@app.route('/add', methods=['GET', 'POST'])
def add():
    ...
    posts.append(new_post)
    save_posts(posts)
3. Delete Post (Delete)
File: index.html (delete link), app.py

When delete link is clicked, route /delete/<id> removes the post from JSON

python
Copy
@app.route('/delete/<int:post_id>')
def delete(post_id):
    ...
    posts = [post for post in posts if post['id'] != post_id]
    save_posts(posts)
4. Update Post (Update)
File: update.html, app.py

Shows a pre-filled form using existing post data

On POST, updates the values in posts.json

python
Copy
@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    ...
    post['title'] = request.form['title']
    save_posts(posts)
5. Data Persistence (JSON File)
File: posts.json, app.py

Used instead of a database

Utility functions load_posts() and save_posts() abstract this behavior

python
Copy
def load_posts():
    with open('posts.json') as f:
        return json.load(f)
✅ Example Post JSON Format
json
Copy
[
  {
    "id": 1,
    "author": "John Doe",
    "title": "Hello World",
    "content": "This is my first post."
  }
]

