#!/bin/bash
echo "Setting up the  rasa server"
rasa run -m models --enable-api --log-file out.log