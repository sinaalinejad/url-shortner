a django app that shorten your long url

first you should clone the repository and then make a virtual environment beside the project app and activate it and then install django framework(for me the version is
3.1.5)
then change directory to the project directory and run this command "python manage.py makemigrations" and then "python manage.py migrate" to initialize the database. now run the project with this command "python manage.py runserver".
how to work with :
to work with this app , you'd better have a program to send different requests to a server(in this case the postman is suggested)
now you should send a post request to the address : "http://127.0.0.1:8000/app/askshortened" with a body in json format with the key : "url" and the value : your long url.
the short url will be given to you. enjoy it :) Thanks

