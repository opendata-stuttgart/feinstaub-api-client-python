# download data of own sensors on feinstaub-api

## config

set your API_TOKEN in config.py

(see config.py-template for example)

## run

```
docker build --tag=feinstaub-api-client .
docker run --rm -ti --name feinstaub-api-client-run feinstaub-api-client
```
