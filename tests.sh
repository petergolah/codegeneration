#!/bin/bash

export PYTHONPATH=$PYTHONPATH:codegeneration:tests

poetry run pytest tests -v
