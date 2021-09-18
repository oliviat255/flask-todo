FROM tiangolo/uwsgi-nginx:python3.7

# Define environment variables
ENV POSTGRES_USER=root
ENV POSTGRES_PASSWORD=root
ENV POSTGRES_DB=blaze

# Install dependencies 
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Copy the app contents to the image
COPY . /app
WORKDIR /app

# Configure command to start docker container
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]