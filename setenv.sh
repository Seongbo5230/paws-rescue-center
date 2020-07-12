#!/bin/bash

echo "Setting env for Flask App"

export FLASK_APP=7_db_sql_alchemy/app.py
export FLASK_ENV=development
export FLASK_DEBUG=1

echo $FLASK_APP
echo "Set FLASK_APP env"
