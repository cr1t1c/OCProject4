# LITREVIEW

This repository contains the code for the UI of the LITREVIEW app.  

## Structure

- The users app is created for users to register and create books and reviews.  It includes sign up and login links in the navigation bar.  
- The reviews app is not completely developed but you are able to create books and add reviews via the two buttons in the UI.  

## Setup

- To install the dependencies you will need to:
  - Start a virtual environment: ```python -m venv env```
  - Install the dependencies: ```pip install -r requirements.txt```
- To migrate you will need to run ```python manage.py makemigrations```
- You will also need to run ```python manage.py migrate```
- In run the server run ```python manage.py runserver``` you may need to run on a different port.  If you need to add what port you want to run (ex. 8080).
- When the server is up and running do a ctrl-click on the link that it gives you and it will pop up the login page.

## Flow

- You will first be met with the login page.  If you do not have an account you can choose the sign up button.
- If you are logged in it will pull up the feed page which has the option of choosing to either create a review or a book.
- You may click on either of these and it will bring up a page to either create a review or book.