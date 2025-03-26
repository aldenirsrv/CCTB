figlet CCTB


figlet CCTB
# -- LOCAL EXEC --
chmod 755 app-config.sh
. app-config.sh

# Local variables
echo "APP_VERSION: $APP_VERSION"
echo "APP_NAME: $APP_NAME"
echo "SLUG: $SLUG"
echo "DOCKER_ACCOUNT: $DOCKER_ACCOUNT"


# -- DOCKER EXEC --
figlet "REACT"
echo "PUSH THE IMAGE" 
docker push $DOCKER_ACCOUNT/$APP_NAME-react-app:$APP_VERSION
echo
figlet "GOLANG"
echo "CREATING THE IMAGE"
docker push $DOCKER_ACCOUNT/$APP_NAME-go-server:$APP_VERSION
echo
figlet "PYTHON"
echo "CREATING THE IMAGE"
docker push $DOCKER_ACCOUNT/$APP_NAME-python-server:$APP_VERSION