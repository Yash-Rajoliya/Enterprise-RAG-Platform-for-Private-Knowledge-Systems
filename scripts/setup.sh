#!/bin/bash

echo "Setting up Enterprise RAG Platform..."

pip install -r requirements.txt

npm install --prefix apps/web-client

npm install --prefix apps/admin-dashboard

echo "Setup completed."