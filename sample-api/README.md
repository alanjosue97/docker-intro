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


3. env-file
Run with env-file
```bash
docker run --env-file .env -p 27017:27017 -d mongo:4.4.6
```

