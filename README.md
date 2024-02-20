# Flask study

## Todo
- [x] Flask
- [x] SQLAlchemy 
- [x] WSGI(Gunicorn)
- [x] Logger
- [ ] Log File Rotation
- [ ] Package Refactoring(MVC)
- [ ] ASGI(Uvicorn, Async)

## Flask
![flask](https://flask.palletsprojects.com/en/3.0.x/_images/flask-horizontal.png)  
Python Micro Web Framework  
가벼운 API 서버로 구성하기 위해 이용

### 추가 구성
+ SQLAlchemy(DB ORM)
+ Marshmellow(Data Serialize, Deserialize, Validate)
+ Gunicorn(WSGI)


## Git Action Workflow
Github에서 제공하는 CI/CD 도구

1. `master`에 commit(push, pull request)가 일어날 때 동작하도록 설정
``` yaml
name: Flask CI

on:
  push:
    branches: [ "master" ]
  pull_request:
    branches: [ "master" ]
```
2. `build` job : Docker Image Build
``` yaml
env:
  DOCKER_IMAGE_NAME: flask_gunicorn
  DOCKER_IMAGE_TAG: ${{ github.sha }}

jobs:

  build:
    runs-on: self-hosted
    steps:
    - uses: actions/checkout@v3
    - name: Build the Docker image
      run: docker build -t ${{ env.DOCKER_IMAGE_NAME }}:${{ env.DOCKER_IMAGE_TAG }} .
```
3. `deploy` job : Docker Compose를 통해 self-hosted 서버에 배포
``` yaml
  deploy:
    runs-on: self-hosted
    needs: build
    steps:
    - name: Manual deployment
      run: docker-compose up --build -d
```
