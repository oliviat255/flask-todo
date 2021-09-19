FROM tiangolo/uwsgi-nginx:python3.9

# Define environment variables
ENV POSTGRES_USER=root
ENV POSTGRES_PASSWORD=root
ENV POSTGRES_DB=blaze

# Install dependencies 
RUN pip3 install pipenv
COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock 
RUN pipenv install --system --deploy --ignore-pipfile 

# Copy the app contents to the image
COPY . /app
WORKDIR /app

# Configure command to start docker container
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]