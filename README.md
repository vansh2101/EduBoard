# EduBoard
My project organizes all the tasks of a student and a teacher very effectively showing the students all the classes scheduled, all the assignments given by the teacher, all the e-books uploaded by a teacher etc. It also has a feature of chat groups using which students can clear their doubts with the teachers and teachers can convey some message to the students in real time.

I built it using Django framework. I have also used a bit of Javascript for the backend. Web sockets are also used using Django-channels.

# Setup
1)Clone the project in your local machine

2)Create a virtual environment using `python -m venv myvenv`. Run `myvenv\scripts\activate` if the virtual environment isn't already activated. (optional step)

3)run `pip install -r requirements.txt` to install all the dependencies

4)Create a database in your postgresql and write the credentials of your database in `eduboard\settings.py`

5)then run `py manage.py makemigrations` and after that run `py manage.py migrate` to setup the database tables

6)Finally, run `py manage.py runserver` to start the web app on your local server on port `8000`
