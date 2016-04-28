FROM gcr.io/google_appengine/python
RUN virtualenv /env -p python2.7

# stackdriver logging & monitoring not necessary in flexible environment
# to install the stackdriver logging agent and monitoring stuff
#RUN apt-get update -y && apt-get install -y apt-utils curl lsb-release
#RUN curl -sSO https://dl.google.com/cloudagents/install-logging-agent.sh && bash install-logging-agent.sh


# Set virtualenv environment variables. This is equivalent to running
# source /env/bin/activate
ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH
ADD requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ADD . /app/
RUN python manage.py collectstatic --noinput
RUN python manage.py migrate --noinput

CMD gunicorn -b :$PORT project_name.wsgi
