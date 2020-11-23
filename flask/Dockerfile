FROM python:3
ADD . /code
WORKDIR /code
## DONT RUN AS ROOT
ENV UWSGI_USER="uwsgi"
ENV UWSGI_ID="1000"
RUN groupadd -g $UWSGI_ID $UWSGI_USER
RUN useradd -ms /bin/bash -u $UWSGI_ID -g $UWSGI_ID $UWSGI_USER
RUN pip install -r requirements.txt
ENV FLASK_DEBUG=0 
ENV FLASK_APP=run.py
ENV FLASK_ENV=development
# run the command to start uWSGI as non-root user!!
CMD ["runuser", "uwsgi", "-g", "uwsgi", "-c", "uwsgi app.ini --uid=${UWSGI_ID} --gid=${UWSGI_ID}"]
