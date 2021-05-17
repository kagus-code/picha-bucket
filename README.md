#  Picha-Bucket Web App

#### This is a Personal Gallery that displays photos for others to see, 14/05/2021

#### By **Eston Kagwima**

## Description

This WebApp allows a user to view images through a gallery and click a particular image to see its description, a user is 
also able to search for images by entering the category in a search input form. They can also filter images based on their location tags

This project was generated with [Django](https://docs.djangoproject.com/en/3.2/) version 3.2.3


### User stories Specification
- View different photos that interest me.
- Click on a single photo to expand it and also view the details of the photo.
- Search for different categories of photos. (ie. Travel, Food)
- Copy a link to the photo to share with my friends.
- View photos based on the location they were taken.
## Setup/Installation Requirements
- install Python3.9
- Clone this repository `git clone https://github.com/kagus-code/picha-bucket.git`
- Change directory to the project directory using  the `cd` command
- Open project on VSCode
- If you want to use virtualenv: `virtualenv ENV && source ENV/bin/activate`
####  Create the Database
    - psql
    - CREATE DATABASE <name>;
####  .env file
Create .env file and paste paste the following and fill  required fields:

    SECRET_KEY = '<Secret_key>'
    DBNAME = '<name>'
    USER = '<Username>'
    PASSWORD = '<password>'
    DEBUG = True
#### Run initial Migration
    python3.9 manage.py makemigrations gallery
    python3.9 manage.py migrate
#### Run the app
    python3.9 manage.py runserver
    Open terminal on localhost:8000


## Technologies Used

- Django version 3.2.3
- Python
- JavaScript
- HTML
- CSS
- Bootstrap
- Postgressql

## link to live site on GitHub Pages

https://pichabucket.herokuapp.com/


## Support and contact details

| Eston | ekagwima745@gmail.com |
| ----- | --------------------- |

### License

License
[MIT License](https://choosealicense.com/licenses/mit/)
Copyright (c) 2021 Eston Kagwima
