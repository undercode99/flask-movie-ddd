#!/bin/sh
gunicorn --chdir app serve:app -w 2 --threads 2 -b 0.0.0.0:5000