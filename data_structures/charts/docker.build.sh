figlet CCTB
# -- LOCAL EXEC --
chmod 755 app-config.sh

# Load application variables
. app-config.sh

# Local variables
echo "APP_VERSION: $APP_VERSION"
echo "APP_NAME: $APP_NAME"
echo "SLUG: $SLUG"
echo "DOCKER_ACCOUNT: $DOCKER_ACCOUNT"


# -- DOCKER EXEC --
figlet "REACT"
echo "CREATING THE IMAGE" 
docker build -t $APP_NAME-react-app ./frontend
echo ">> TAGGING REACT IMAGE {$APP_NAME-react-app}"
docker tag $APP_NAME-react-app $DOCKER_ACCOUNT/$APP_NAME-react-app:$APP_VERSION
echo
figlet "GOLANG"
echo "CREATING THE IMAGE"
docker build -t $APP_NAME-go-server ./ms-go
echo ">> TAGGING REACT IMAGE {$APP_NAME-go-server}"
docker tag $APP_NAME-go-server $DOCKER_ACCOUNT/$APP_NAME-go-server:$APP_VERSION
echo
figlet "PYHON"
echo "CREATING THE IMAGE"
docker build -t $APP_NAME-python-server ./python-ms
echo ">> TAGGING PYHON IMAGE...{$APP_NAME-python-server}"
docker tag $APP_NAME-python-server $DOCKER_ACCOUNT/$APP_NAME-python-server:$APP_VERSION