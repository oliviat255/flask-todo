FROM tiangolo/uwsgi-nginx:python3.8

# Define environment variables
ENV POSTGRES_USER=root
ENV POSTGRES_PASSWORD=root
ENV POSTGRES_DB=blaze

# Copy the app contents to the image
COPY . /app
WORKDIR /app

# Install dependencies 
RUN pip install pipenv
COPY Pipfile* /tmp
RUN cd /tmp && pipenv lock --keep-outdated --requirements > requirements.txt
RUN pip install -r /tmp/requirements.txt
COPY . /tmp/myapp
RUN pip install /tmp/myapp

# Configure command to start docker container
ENTRYPOINT ["python3"]
CMD ["wsgi.py"]