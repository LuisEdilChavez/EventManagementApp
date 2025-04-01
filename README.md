A event management app for the CSIT415 project to demonstrate our SWE and developement skills.


**FILE STRUCTURE PLEASE LOOK AT CAREFULLY**
db.sqlite3 -- Database stuff, (tables for storing user data)
Eventapp/                   
manage.py               # managing the page/settings management.
  event_app               # Main project package ie settings stuff
 __init__.py
 settings.py
  urls.py
   asgi.py
   wsgi.py
  -----------
  Eventapp (folder)                 #Django app folder
   __init__.py
    admin.py
    apps.py
    models.py
    tests.py
    views.py
    urls.py            
    templates/          # HTML files go here
    static/             # CSS, JS, images go here
