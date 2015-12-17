#  <div align="center">Movieratings</div>

Movieratings is a Django web application that uses the [MovieLens 1M](http://files.grouplens.org/datasets/movielens/ml-1m.zip) dataset to allow the user to check movie ratings, add and edit movie ratings and track the movies they have not yet rated.

## <div align="center">Instructions</div>

* Before the user can run the Movieratings application on their computer, the user must first clone the `movieratings` repo onto their computer. The user will need to create a virtual environment running Python 3 in the `movieratings` repo folder.
* To properly run the application, the contents of requirements.txt must be installed.
  * After navigating to the folder containing `requirements.txt`, enter `pip install -r requirements.txt` on the command-line to download the contents of requirements.txt.
* Movieratings uses an SQLite database. The data will need to be loaded before running the application. After navigating to the `movieratings` folder that contains `manage.py`, enter the following commands on the command-line to properly load the data:
  * `python manage.py migrate`
  * `python manage.py loaddata users movies ratings`
* The user must run a local server in order to use the application. After navigating to the `movieratings` folder which contains `manage.py`, enter `python manage.py runserver` on the command-line to start the local sever. The application can now be accessed via the user's web browser at `http://localhost:8000/`.
