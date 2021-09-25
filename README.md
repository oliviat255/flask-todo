# Todo App 
I created this application to become familiar with the [Flask](https://flask.palletsprojects.com/en/2.0.x/) framework, creating routes from scratch, and local containerization using [Docker](https://www.docker.com/). 

## Requirements 
* [Docker for Mac](https://docs.docker.com/desktop/mac/install/) 
* Python 3.9
* Pip3 

## Tech Stack  
* Flask 
* Pipenv 
* RestX 
* Pytest 
* SqlAlchemy 

### Flask Learnings 
I chose Flask because it is a lightwork framework that is easy to get started with. 

### Testing Learnings 
Pytest can run serveral tests in parallel. This saves a considerable amount of computation time. This makes it superior to the unittest library.

### Dependecy Management 
Dependencies are managed using pipenv. I chose to use pipenv over requirements.txt because by default requirements.txt does not specify versions. This can be an issue when the latest version of a package is installed and it is not backwards compatible. I have expiermented with using `pip freeze` to spciefy the versions of the packages. However, this solution easily becomes unmaintable when you have to worry about every version of every package, including sub-dependencies. Using pipenv you do not have to force extract versions. You can also specify packages for development environment and a production environment. A more eloquent explanation of pipenv can be found [here](https://realpython.com/pipenv-guide/#dependency-management-with-requirementstxt). 