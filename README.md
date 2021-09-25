# Todo App 
I created this application to become familiar with the [Flask](https://flask.palletsprojects.com/en/2.0.x/) framework, creating routes from scratch, and local containerization using [Docker](https://www.docker.com/). 

## Requirements 
* [Docker for Mac](https://docs.docker.com/desktop/mac/install/) 
* Python 3.9
* Pip3 

## Installation and Workflow 
Run these commands the first time you install, as well as when you reactivate your virutal environment. 
```
make shell
make update-dev
```
### Run flask app from shell 
```make run-dev ``` and then confirm in browser at http://127.0.0.1:5000/api/v1/health/api 

Swagger can be found at the root http://127.0.0.1:5000/api/v1/
 


## Tech Stack  
* Flask 
* Pipenv 
* RestX 
* Pytest 
* SQLAlchemy 

### Flask Learnings 
I chose Flask because it is a lightwork framework that is easy to get started with. 
The endpoints in this application are contained in a blueprint. A blueprint is a set of operations that can be registered on an application. A single flask application can contain multiple blueprints. A blueprint can also be registered to the same application multiple times. It is a simliar concept to application components in that the goal of a blueprint is to organize a larger application into smaller parts. 
I used flask-restx to create a restful api. This made it easy create todo as a CRUD resource. Flask-restx also provides the concept of a namespace to organize an application. I created two namespaces, todo and health, and mounted them to the application. The concept of a namespace is useful when you need to create a new version of the api.


### SQLAlchmey 
I used SQLAlchemy to create an in-memory database for this application. SQLAlchemy also serves an an Object Relational Mapper (ORM) tool that translates classes to tables on relational databases and automatically converts function calls to SQL statements. This is a more secure way of communicating with a relational database than sending SQL queries as strings. SQLAlchemy sessions guarentee database consistency. In this application I create a new session each time I need to make a call to the database. This is considered best practice on the [documentation](https://docs.sqlalchemy.org/en/14/orm/session_basics.html#session-frequently-asked-questions). 

### Testing Learnings 
Pytest can run serveral tests in parallel. This saves a considerable amount of computation time. This makes it superior to the unittest library.

### Dependecy Management 
Dependencies are managed using pipenv. I chose to use pipenv over requirements.txt because by default requirements.txt does not specify versions. This can be an issue when the latest version of a package is installed and it is not backwards compatible. I have expiermented with using `pip freeze` to spciefy the versions of the packages. However, this solution easily becomes unmaintable when you have to worry about every version of every package, including sub-dependencies. Using pipenv you do not have to force extract versions. You can also specify packages for development environment and a production environment. A more eloquent explanation of pipenv can be found [here](https://realpython.com/pipenv-guide/#dependency-management-with-requirementstxt). 

