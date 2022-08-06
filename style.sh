#!/usr/bin/bash

isort --py 310 app.py
black -t py310 app.py
