# URL Shortener

Url Shortener with ZooKeeper for multiple instance


# How to Support a lot of POD ?

- Each pod has own id range. for example for app-0 (100000) * (0 +1) to (100000) * (0 + 2).
it's mean app-0 pod will give id's in rage of 100000 to 200000.

- Each pod is creating his own zookeeper path when starting pod. (handle_zookeeper command) (you can check start.sh)



# API's

You can also view API's in /docs/ and /redoc/ paths.

- [POST]  /api/v1/url-shortener/         
--> Produce short url from long url </br>
--> [body] -> url

- [GET]  /api/v1/all-url/             
--> Retrieve All informations about URL's

- [GET]  /{str:url}     
--> Redirect to long url and increase visitor count


# Create ZooKeeper Paths

```
python manage.py handle_zookeeper
```
This command will create path according to your enviroment variable.

- TOTAL_POD_COUNT = Total replica count (needed for create path with specific number)
- HOSTNAME = Unique name of pod or given unique path

HOSTNAME value 
- default app-100 
- for docker-compose app-101 
- for k8s app-0 to app-N 

# Deployment

## Manual Deploy

You can use vscode run section and run django app. (You have to open ZooKeeper in your local for this)

Open ZooKeeper in your local with docker


```
docker run  -d -p 2181:2181 -p  2888:2888 -p 3888:3888 -p 8080:8080  zookeeper
```

```
docker run -d -p 27017:27017 mongodb 
```

## Docker Deploy

```
docker run -p 8000:8000 . 
```

## Docker-compose Deploy

This is not a good replication it's use same zookeeper path becouse of dynamic envrion problem of docker-compose (we can't give dynamic env for replicas)

```
docker-compose up --build
```

## Kubernetes Deploy

- Easly run **start_deploy_k8s.sh** script.

Note: Script wrote with helm be sure you have helm and k8s on your computer.

- Install mongodb
```
helm install mongodb  bitnami/mongodb --values=./helm/mongodb_values.yaml -n urlshortener
```
- Install ZooKeeper
```
helm install zookeeper bitnami/zookeeper -n urlshortener
```
- Install URL Shortener App
before you run below code you should build image and push to local registry. (You can check **start_deploy_k8s.sh**)
```

helm upgrade --install app ./helm/app -n urlshortener
```


# Unittest 

You can run test with vscode run section or 

```
python manage.py test core.api.v1.test
```

Be sure you have mongodb up and running


