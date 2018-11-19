# airflow-workshop

BigData Vilnius workshop 2018

### Cheat sheet for docker commands

Bring up a container:

```
$> docker-compose -f docker-compose.yaml up -d
```

Take it all down:

```
$> docker-compose -f docker-compose.yaml down
```

Dags can be put in the 'dags' directory, they are mounted in the container.

