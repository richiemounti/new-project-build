# politico

# DESCRIPTION
Politico ic a platform that aims o increase transparency in the electoral process by automating its systems
Politico uses data structures to store information


# Installation instructions
1 Clone the repo
    git clone https://github.com/richiemounti/new-project-build.git

2 Navigate to the root folder
    cd new-project-build

3 Set up a virtual environment
    #linux
     virtualenv venv
    #windows
     python -m virtualenv venv
     
4 Activate virtual environment
    #linux
     source venv/bin/activate
    #windows
     venv/Scripts/activate
    
5 Setup env variables

     #linux
     - export FLASK_APP=politicer.py
     - export FLASK_DEBUG=1
     - export FLASK_ENV=development
     #windows
     - set FLASK_APP=politicer.py
     - set FLASK_DEBUG=1
     - set FLASK_ENV=development
6 Manually Running tests

   python -m pytest --cov=app
7 Start the server

   flask run
