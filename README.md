# User Authentication with Flask

A lightweight and practical Flask application that handles user registration, login, session management, and a protected dashboard. Built to demonstrate a straightforward yet secure approach to user authentication in web apps.

---

## Overview

This repository includes a minimal but complete example of user authentication using Flask and MongoDB (via PyMongo). It demonstrates:

- Secure user registration with email and hashed passwords  
- User login with session-based authentication  
- Protected dashboard accessible only to logged-in users  
- Logout functionality  
- Flash messages for user feedback  
- Organized project structure with templates and static assets  

It’s ideal for learning, demos, or bootstrapping your own Flask-based authentication system.

---

## Features

- **User Registration**  
  Users can sign up with an email and password, which are securely hashed using bcrypt before being stored in the database.

- **User Login & Session Handling**  
  Authenticated users can log in and gain access to a protected dashboard. Sessions are maintained using Flask’s built-in session.

- **Flash Messages**  
  Give users real-time feedback during registration, login, and logout actions.

- **Logout**  
  Clears the session and logs users out safely.

- **Clean Code Structure**  
  Separated folders for `static/`, `templates/`, and main `app.py` for clear organization.

---

## Requirements

- Python 3.8+
- Flask
- Flask-PyMongo (or PyMongo)
- `bcrypt`
- Optional: Bootstrap for styling (via CDN)

