FROM gcr.io/google_appengine/python
RUN virtualenv /env -p python3.4

#ADD https://dl.google.com/cloudagents/install-logging-agent.sh /tmp/
#RUN /tmp/install-logging-agent.sh



# Set virtualenv environment variables. This is equivalent to running
# source /env/bin/activate
ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH
ADD requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ADD . /app/
RUN python manage.py collectstatic --noinput

RUN curl -sSO https://dl.google.com/cloudagents/install-logging-agent.sh && bash install-logging-agent.sh
COPY forward.conf /etc/google-fluentd/config.d/forward.conf

CMD gunicorn -b :$PORT project_name.wsgi
