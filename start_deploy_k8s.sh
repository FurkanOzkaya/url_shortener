echo "=========================="
echo "=========================="
echo "=========================="
echo "Initilazing local registry"
echo "=========================="
echo "=========================="
echo "=========================="
docker run -d -p 5000:5000 --restart=always --name registry registry:2



echo "=========================="
echo "=========================="
echo "=========================="
echo "Building APP Image"
echo "=========================="
echo "=========================="
echo "=========================="

docker build -t url_shortener:0.0.1 .

echo "=========================="
echo "=========================="
echo "=========================="
echo "Tagging App"
echo "=========================="
echo "=========================="
echo "=========================="

docker tag url_shortener:0.0.1 localhost:5000/url_shortener:0.0.1 


echo "=========================="
echo "=========================="
echo "=========================="
echo "Pushing Image to local Repository"
echo "=========================="
echo "=========================="
echo "=========================="

docker push localhost:5000/url_shortener:0.0.1 

kubectl create namespace urlshortener

helm  upgrade --install mongodb  bitnami/mongodb --values=./helm/mongodb_values.yaml -n urlshortener

sleep 10


helm  upgrade --install zookeeper bitnami/zookeeper -n urlshortener

sleep 10

helm upgrade --install app ./helm/app -n urlshortener


echo "=========================="
echo "=========================="
echo "=========================="
echo "SUCCESS"
echo "=========================="
echo "=========================="
echo "=========================="