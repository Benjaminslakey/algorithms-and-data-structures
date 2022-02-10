#!/usr/bin/env bash

PROJECT_ROOT="$( cd  "$( dirname "$0" )" && pwd )"
echo $PROJECT_ROOT
export PYTHONPATH=$PYTHONPATH:/$PROJECT_ROOT/bts_lib

pytest bts_lib
pytest leetcode/*/*.py
