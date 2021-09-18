shell: 
	pip3 install pipenv && pipenv shell 

update-dev: 
	pipenv install && pipenv update 

run-dev:
	export FLASK_APP=wsgi.py; \
	export FLASK_ENV=development; \
	flask run 