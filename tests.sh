#!/usr/bin/env bash

. ./.venv/bin/activate

export PYTHONPATH=$(pwd):$PYTHONPATH
python Tests/tests.py
