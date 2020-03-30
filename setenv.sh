#!/bin/bash

echo "Setting env for Flask App"

export FLASK_APP=6_form_handling/app.py
export FLASK_ENV=development
export FLASK_DEBUG=1

echo $FLASK_APP

