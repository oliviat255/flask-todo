shell: 
	pip3 install pipenv && pipenv shell 

update-dev: 
	pipenv install && pipenv update 

dev-env-vars: 
	export FLASK_APP=wsgi.py; \
	export FLASK_ENV=development; \

run-dev: dev-env-vars 
	flask run 

docker: dev-env-vars 
	docker-compose build && docker-compose up;

stop-docker: 
	docker-compose down --remove-orphans;

lint:
	pylint --disable=C0303 src

test: 
	export FLASK_ENV=TEST; \
	python -m pytest -vv

mypy: 
	mypy .