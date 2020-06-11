# how to set up the django app for mysql

1) install mysqlclient
=>pip install mysqlclient

2) open xampp or laragon or standalone mysql if you want

3) open the settings.py in project and relace the
sqlite3 database config with

for xampp and laragon user is root and no password

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
