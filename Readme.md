# Blog API

Blog API is a python based Blog Application built using the Django Framework and the REST API.

It lets the user:

- Sign-Up
- Login
- Create Post
- Update Post
- Delete Post
- View Post

## Features

- User Login and Authentication
- Admin site management
- CRUD based architecture
- Easy to Use

This application uses Django REST framework to POST, RETRIEVE, UPDATE and DELETE the user's blogs, along with the user
login and authentication. In general terms, it lets the user create and manage its content on the website.

## Tech

- [Django] - HTML enhanced for web apps!
- [PyCharm] - text editor
- [HTML and CSS] - For the dummy frontend

## Installation

Blog API requires python and django to run.

```python
pip
install
django
pip
install
djangorestframework
```

Clone the repository, and start the server

```python
cd
blog
python
manage.py
startserver
```

Click on the ip address generated, which will launch the home page of the application.

## Functionalities

Following are the different routes implemented:

- [admin/] - routes to the admin page.
- [users/] - routes to the users page to show all the users and their details.
- [users/<int:pk>/] - routes to the specific user page with pk as their id.
- [posts/] - routes to the posts page to show all the posts and their details.
- [posts/<int:pk>/] - routes to the specific post page with pk as their id.
- [api-auth/] - routes to the authentication page.