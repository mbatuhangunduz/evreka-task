# Evreka Task Api


# To run in local python virtual environment:

You should create virtual environment in the directory  \...\evreka-task>, not in the "project". (Especially you should create "venv" in the same directory as "requirements.txt".)

## To create virtual environment the command should be :
if virtual environment exists by default: <br/>
python3 -m venv venv

if you create by hand: <br/>
virtualenv venv

## Then to activate:
for windows: <br/>
venv\Scripts\activate

for mac: <br/>
. venv/bin/activate

or

source venv/bin/activate

## Then you should install packages in requirements if any new package was added to project :

pip install -r requirements.txt

## Then you should get into "project" with the command "cd project" to create or update database.

python manage.py makemigrations<br/>
python manage.py migrate<br/>
python manage.py runserver<br/>

In this case the backend will be served in 127.0.0.1:8000/
