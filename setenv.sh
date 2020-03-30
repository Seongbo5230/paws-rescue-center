#!/bin/bash

echo "Setting env for Flask App"

export FLASK_APP=6_rendering_a_sign-up_form_and_navbar/app.py
export FLASK_ENV=development
export FLASK_DEBUG=1

echo $FLASK_APP
echo "Set FLASK_APP env"
