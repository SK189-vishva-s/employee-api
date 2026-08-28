docker pull vishva420/employee-api:latest

docker stop employee-api 2>$null
docker rm employee-api 2>$null

docker run -d --name employee-api -p 8000:8000 vishva420/employee-api:latest