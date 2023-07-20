Commands:

Docker processes:

```bash
    docker ps
```

1. Database conection:
```bash

cd database
docker build -t academia-database . 
docker run -p 207017:27017 -d academia-database

```
2. API
Get the database  IP with?`docker inespection <container ip>`.
change the conexion string in `utils/database.py` .
```bash
cd api
docker build -t academia-api
docker run -p 8000:8000 -d academia-api
```

3. push ECR
to push image to ECR:

```bash
aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin {repositorio_name}
export AWS_ACCOUNT_ID=782915225744
export AWS_DEFAULT_REGION=us-west-2
export AWS_ECR_REPOSITORY_NAME=backend-academia
export DOCKER_IMAGE_TAG=latest
docker build -t sample-compose ${DOCKER_IMAGE_TAG} .
```
4. To Re-write my API 
Run this comand to re-write on docker-compose.prod.yml
```bash

docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d   
```
5. Deploy to AWS
```bash
docker context create ecs academia
```

# Select - AWS environment variables
```bash 
Docker Compose's integration for ECS and ACI will be retired in November 2023. Learn more: https://docs.docker.com/go/compose-ecs-eol/
? Create a Docker context using:  [Use arrows to move, type to filter]
  An existing AWS profile
  AWS secret and token credentials
> AWS environment variables

docker context use academia

docker compose -f docker-compose.yml -f docker-compose.prod.yml up
```