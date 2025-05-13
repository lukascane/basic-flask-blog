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