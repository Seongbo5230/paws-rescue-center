#!/bin/bash

echo "Setting env for Flask App"

export FLASK_APP=8_models_transaction/app.py
export FLASK_ENV=development
export FLASK_DEBUG=1
export SQLALCHEMY_TRACK_MODIFICATIONS=False

echo $FLASK_APP
echo "Set FLASK_APP env"
