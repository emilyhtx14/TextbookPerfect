### Summary

This project is a web app that consolidates 20+ high quality study resources with just one simple scan of your textbook cover. Remote studying made easier.

Here is how to run the demo on a MAC PC and a smart phone.

### Repository
The project has been uploaded into github repository **TextbookPerfect**. if you have the git installed on MAC PC, you can clone the project TextbookPerfect from the github by this command and run the demo on MAC PC and a smart phone.

    git clone git@github.com:emilyhtx14/TextbookPerfect.git

### Prerequest for Demo
* In addition to the source code, **python3** and an **virtual env** with **Django** installed are required in order to run the project demo. 
* To run, install the appropriate packages
* python manage.py makemigrations
* python manage.py migrate
* python manage.py runserver 

If running from mobile, through an IP address,

* python manage.py runserver {Computer IP-Address}:8000

* To get to the resource view you must add /reviews after the local host has been loaded, in order to avoid the error view

* When filling out the form field for Textbook Exchange, please make sure to separate subjects by commas and then a space (ex. Multivariable, Linear Algebra)

* When taking an image for the textbook resource view, please try as much as you can to capture as closely to the textbook as possible (no surrounding white frame).

* Note that if the YT Quota Search is exceeded for the API_KEY, the app will not run.

* Finally, the current textbook database, consists of STEM subjects; if your textbook title does not contain one of these words, it will not properly process the request.

key_terms = ['algebra', 'topology', 'geometry', 'multivariable', 'calculus', 'analysis', 'trigonometry',
                 'number theory', 'arithmetic', 'probability', 'statistic', 'combinatorics',
                 'discrete mathematics', 'linear algebra', 'algebraic geometry', 'set theory', 'fraction',
                 'differential', 'electromagnetism', 'quantum', 'mechanics',
                 'nuclear', 'physics', 'thermodynamics', 'astrophysics', 'biophysics', 'optics', 'relativity',
                 'particle physics', 'cosmology', 'solid-state', 'atomic', 'molecular',
                 'acoustics', 'astronomy', 'gravity', 'geophysics', 'python', 'java', 'javascript', 'react', 'css',
                 'html', 'scala','coding','biology','organizational','economics','business', 'entrepreneur', 'management',
                 'supply','accounting','law','number theory','optimization','trigonometry', 'MATLAB']



* **TextbookPerfect** directory is created with the git clone. A sub-directory **src** under TextbookPerfect contains all the source code to run the demo. The **venv** also has been added into the repository for the convenience (The python3 and virtual env with Django can be installed with the follow command if you don't want to use the one from the repository).

### Install virtualenv
    cd TextbookPerfect
    brew install python3
    sudo pip3 install virtualenv
    source venv/bin/active
    pip install Django==3.0

### Demo on Local Mac
    cd TextbookPerfect/src
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver

### Use the App
With the application running on MAC and have a smart phone browser point to the server web server running on MAC, you can use the phone to scan a text book cover page and the app will consolidate 20+ high quality study resources related to the text book scanned, like youtube videos, online study groups and references, etc.

### Contact
* Email : emilyhtx14@gmail.com
