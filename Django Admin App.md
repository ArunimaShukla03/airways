We don't wanna go to the shell again and again to manipulate the models thus django has already created "Django Admin App" in order for me to do so.

In order to use the admin app we need to create an administrative account inside our django web application.

This can be done by "python manage.py createsuperuser".

Now we have created our credentials, we have the ability to visit the web interface for our admin app and actually manipulate some of these underlying models.

First we need to add our models to the admin app. We added the models to the admin app by going to the "admin.py" and registering both of the models. 

Now when we go to the site and login using the credentials, now we have the ability to manipulate the underlying database by manipulating the models and add or modify data that already exists.

