#!/bin/sh
pip install --no-build-isolation --force-reinstall "boto3>=1.28.57" "awscli>=1.29.57" "botocore>=1.31.57"
pip install --no-build-isolation --force-reinstall "langchain==0.0.263" "streamlit==1.26.0"