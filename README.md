# Skin cancer detection application 

## Description
This application integrates an SVC image classifying model into a Django application for skin cancer detection. The application also integrates Chart.JS graphs which allow users to learn more about their relative risk of developing skin cancer.
### Application architecture
The application is dockerized into three containers and deployed using docker-compose. 
Shared components between the containers are implemented using bind mounts for simplicity. 
Successful deployment of the application depends on a configured .env file which is not included in this repo. 

### Application dependencies
View Dockerfiles and requirements files outlined in the docker-compose.yml

### Dataset 
The data used to train the SVC model can be found on Kaggle using the link below. 
https://www.kaggle.com/kmader/skin-cancer-mnist-ham10000

### Author
Kevin Hardaway
