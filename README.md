# Food Delivery

Framework: Django

How to run this app:

1. Install Python
2. Activate virtual environment:
   * Set-ExecutionPolicy Unrestricted -Scope Process
   * python -m venv venv
   * venv/Scripts/activate 
3. Install dependencies:
   * pip install -r requirements.txt
4. To get access to database:
   * python manage.py createsuperuser
5. Run the migrations:
   * python manage.py makemigrations
   * python manage.py migrate
6. Run local server:
   * python manage.py runserver
 