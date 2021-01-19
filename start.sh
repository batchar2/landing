#!/bin/bash

NAME="hello_app"                                  # Name of the application
DJANGODIR=/var/www/lp/lp             # Django project directory
SOCKFILE=/var/www/lp/gunicorn.sock  # we will communicte using this unix socket
USER=www-data                                        # the user to run as
GROUP=www-data                                     # the group to run as
NUM_WORKERS=1                                     # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=chsite.settings             # which settings file should Django use
DJANGO_WSGI_MODULE=chsite.wsgi                     # WSGI module name

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source /var/www/lp/venv/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec /var/www/lp/venv/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
--log-file=-
