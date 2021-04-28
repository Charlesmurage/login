# login
--clone project to your computer by using “git clone ‘url’”
-install virtual machine using “python3.6 -m venv --without-pip virtual”
-install bootstrap using “curl https://bootstrap.pypa.io/get-pip.py | python”
-install requirements.txt using “pip install -r requirements.txt”
-Now create postgres database and configure credentials in the following sections:
DATABASES = {
'default': {
'ENGINE': 'django.db.backends.postgresql',
'NAME': 'login', //database name
'USER': 'charles',// username
'PASSWORD':'chweezyy94',// password



-create superuser to add users by typing “python manage.py createsuperuser’
this will enable you to allocate roles and add users to be able to login

-now run app using “python manage.py runserver’
-to access admin part add 127.0.0.1:8000/admin
