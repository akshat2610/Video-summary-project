<h1 align="center"> Developer's Guide to the Project</h1>

## Set up

### Prerequisites

You will need

- Git - [Download & Install Git](https://git-scm.com/downloads).
- Python - [Download & install Python3](https://www.python.org/downloads/) and follow the instructions on the graphical installer
- pip - [Download & install pip](https://pip.pypa.io/en/stable/installing/) run python -m pip --version
- nltk - [Download & install nltk](https://www.nltk.org/install.html) run pip install --user -U nltk
- PHP - [Download & install PHP](https://www.php.net/manual/en/install.php) 
- Flask - [Download & install Flask](https://flask.palletsprojects.com/en/1.1.x/installation/) run pip install Flask
- Node.js - [Download & Install Node.js](https://nodejs.org/en/download/) and the npm package manager.

### Installation
Clone this repo to your desktop

### Running the application
After cloning the repo, go to the root directory and run login_service.py, notes_service.py, transcript_processing_service.py, and video_editing_service.py

You can no access the app at localhost:5000

### Testing

We automated the tests that check the functionality of the forms. 
1) Tests check fillable text fields for login and that the button is responsive and will log in the user.
2) Tests check fillable text fields for signup and that the sing up button is responsive and will sign up the user.
3) Check functionality of the backend, but starting the processing of video file, transcript and dictionary. Confirms the test by confirming the creation of summary.

To run the tests, cd into the root directory of the tests. Then run the following java –jar NameOfJar.jar

The browser should start and navigate to my web page!


