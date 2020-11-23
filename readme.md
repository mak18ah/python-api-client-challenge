to run:

```
$ docker-compose up --build
$ docker run -it --rm --net=host -v $(pwd):/code -w /code python /bin/bash -c "pip install -r requirements.txt && pytest"
```