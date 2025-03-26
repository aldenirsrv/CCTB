# -- LOCAL EXEC --
chmod 755 app-config.sh

# Load application variables
. app-config.sh

echo "DROPPING PODS: VERSION: {$APP_VERSION}"


docker stop financial-python-server financial-go-server financial-react-app
docker rm financial-python-server financial-go-server financial-react-app
docker rmi aldenir/financial-go-server:$APP_VERSION  aldenir/financial-python-server:$APP_VERSION