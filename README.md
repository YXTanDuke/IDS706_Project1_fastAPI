[![Python application test with github actions](https://github.com/YXTanDuke/IDS706_Project1_fastAPI/actions/workflows/main.yml/badge.svg)](https://github.com/YXTanDuke/IDS706_Project1_fastAPI/actions/workflows/main.yml)
# A Continuous Delivery of FastAPI Data Engineering API on AWS

For this project, an endpoint that counts the most frequent character in a given String was created. The function for the code is simple, but the main goal for this project is to get familiar with cloud development.

First, an AWS Cloud9 cloud envrionment was used to develop code for this project. Python environment was setup in the Cloud9 environment using MakeFile, including basic packages for testing and linting, along with fastApi and uvicorn for web services. In addition, continuous integration was accomplished using github action as you can find in the Action section. Basic steps including linting and testing will be performed every time code is pushed to the main branch. Also, a badge was added to README indicting the currect status for the project. Also, 100% test coverage was accomplished and edge cases were considered. Finally, continuous delivery was accomplished using AWS auto deployment. When new code is updated in the cloud9 environment, deployment will be triggered and website will be updated.

default domain: https://vy9tc2mnsv.us-east-1.awsapprunner.com 
documentation: https://vy9tc2mnsv.us-east-1.awsapprunner.com/docs
