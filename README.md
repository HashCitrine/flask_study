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

1. `build` job : Docker Image Build([docker-image.yml](/workflows/docker-image.yml))
``` yaml
name: Flask Docker Image Build

on:
  push:
    branches: [ "master" ]
#  pull_request:
#    branches: [ "master" ]
    
env:
  DOCKER_IMAGE_NAME: flask_gunicorn
  DOCKER_IMAGE_TAG: ${{ github.run_id }}

jobs:

  build:
    runs-on: self-hosted
    steps:
    - uses: actions/checkout@v3
    - name: Build the Docker image
      run: docker build -t ${{ env.DOCKER_IMAGE_NAME }}:${{ env.DOCKER_IMAGE_TAG }} .
```

- `master`에 commit(push, pull request)가 일어날 때 동작하도록 설정
- `github.run_id`을 Docker Image Tag로 이용

2. `deploy` job : Docker Compose를 통해 self-hosted 서버에 배포([deploy.yml](/workflows/deploy.yml))
``` yaml
name: Flask Deploy

on:
  workflow_dispatch:
    inputs:
      build_id:
        description: 'Docker Image Build Workflow Run ID'
        required: true

env:
  DOCKER_IMAGE_NAME: flask_gunicorn
  DOCKER_IMAGE_TAG: ${{ github.event.inputs.build_id }}

jobs:

  deploy:
    runs-on: self-hosted
    if: github.event_name == 'workflow_dispatch'
    steps:
    - name: Manual deployment
      run: docker-compose up --build -d
```

- 배포(deploy)를 위해 `수동(workflow_dispatch)`으로 실행
- `build_id` 환경 변수를 workflow 실행 시 입력받도록 설정  
![image](https://github.com/HashCitrine/flask_study/assets/38382859/8899a235-06b1-4a69-8971-b7444eb998f6)

