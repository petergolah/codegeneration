#!/bin/bash

export CODEGENERATION_CONFIG_FILE="${CODEGENERATION_CONFIG_FILE:-config.yml}"
export CODEGENERATION_FORMATIONS_FILE="${CODEGENERATION_FORMATIONS_FILE:-formations.yml}"
export CODEGENERATION_CWD=$(pwd)

export PYTHONPATH=$PYTHONPATH:codegeneration

REALPATH=$(readlink -f "$0")
cd $(dirname $REALPATH)

poetry run python codegeneration/main.py "$@"
