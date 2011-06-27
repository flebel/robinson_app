============================
django-robinson demo project
============================

This is a demo project for the `django-robinson` application. Note that this project comes with no guarantee and is meant as a demonstration of a use of django-robinson. A live demo will be deployed online in the near future.

These are the features that are planned for future versions, in order of priority:

- Center the map to show the most markers when the page is initially loaded
- Color code the accuracy
- Add the ability to search for photos by tag
- Refactor/rewrite the JavaScript code that creates the DOM from the results of the AJAX calls
- Run a live version with admin access

Installation
============

#. This project has been developped with Django 1.3 in mind. Running the project with Django < 1.3 may cause the Moon to burst in flames. No kidding.

#. The installation instructions cover the requirements for the project as well as the `django-robinson` application.

#. Use the `requirements.txt` file with pip to install the dependencies. Note that one of them requires manual installation. See `requirements.txt` for more information.

#. Run the project either with `python manage.py runserver` or through `mod_wsgi`, for instance.

Configuration
=============

The following variables found in the included `settings.py` have to be set or updated before you can run the project:

- ADMINS
- DATABASES
- SECRET_KEY

