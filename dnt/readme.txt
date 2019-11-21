To get this project up and running locally on your computer:
Set up the Python development environment. Virtual environment with Python3 is recommended.
Make sure you are in the project directory, where manage.py and requirements.txt files are located.
Run the following commands
1-   pip3 install -r requirements.txt
2-   python3 manage.py makemigrations
3-   python3 manage.py migrate
4-   python3 manage.py collectstatic
5-   python3 manage.py runserver
Open a browser to http://127.0.0.1:8000/ to open the login page

Note:
    Command 2, 3, 4 are optional only required if some message appears on screen