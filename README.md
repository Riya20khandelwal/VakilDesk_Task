# VakilDesk_Task

# 1. Set Up Virtual Environment
# First, create a virtual environment to isolate your Python dependencies for this project.
python -m venv environ

# 2. Activate the Virtual Environment
# Activate the environment to ensure all dependencies are installed within it.
# For Windows, use the command:
environ\Scripts\activate

# Once activated, your terminal will indicate the active environment by displaying its name in the prompt.

# 3. Navigate to the Project Directory
# Go to the directory where the Django project is located:
cd django_assignment

# 4. Install Dependencies
# Install all the required packages listed in the requirements.txt file:
pip install -r requirements.txt

# 5. Start the Django Development Server
# To run the Django application locally, use the following command:
python manage.py runserver

# The server will run on http://127.0.0.1:8000/. Open this URL in your browser to view the default pages of the project.

# 6. Access the Admin Panel
# To manage orders and other models, Django provides an admin interface. You can access the admin panel by navigating to:
http://127.0.0.1:8000/admin/

# Admin Credentials
#Use the following credentials to log in:
# Username: admin
# Password: admin
# Alternatively, if you prefer to create your own admin user, use the following command:
python manage.py createsuperuser

# 7. Database Migrations (If Necessary)
# If the database structure needs to be created or updated, you will need to run the following commands:
python manage.py makemigrations
python manage.py migrate

# 8. Customizing Pages and Data
# I have already created pages to provide you with a basic structure and functionality. However, if you want to modify the data processing or the content displayed on the pages, you can customize the logic by editing the views.py file.

# Where to Find views.py
django_assignment\task\views.py
