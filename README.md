# <h1>Test Driven Development with Django, Docker, Docker Hub, Github actions, PostgreSQL, and AWS</h1>

 In this project, I will be building a food-recipe API using Django and its REST framework


to start with the project, you'll need to run 
```
docker build
docker-compose build

```

Then after that you'll run the 
```
docker-compose run --rm sh -c "python manage.py makemigrations"

docker-compose run --rm sh -c "python manage.py migrate"
```
