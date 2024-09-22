# VakilDesk_Task

# create environment
py -m venv environment
# activate environment (For Windows)
environ\Scripts\activate 

cd django_assignment
# install all requirements ->
pip install -r requirements.txt

# start server ->
py manage.py runserver

# run on browser ->
http://127.0.0.1:8000/

# admin panel for add oders ->
http://127.0.0.1:8000/admin/

# admin credential -> username = admin, password= admin
# Or you can create admin also by using command
py manage.py createsuperuser

# If in case db missed then run command - >
py manage.py makemigrations
py manage.py migrate
