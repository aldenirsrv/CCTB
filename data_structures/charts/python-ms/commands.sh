# -- LOCAL EXEC --
chmod 755 app-config.sh

# Load application variables
. app-config.sh

# Local variables
SLUG="python"
LOCAL_PORT="5000"
DOCKER_PORT="5000"
echo "APP_VERSION: $APP_VERSION"
echo "APP_NAME: $APP_NAME"
echo "SLUG: $SLUG"
echo "DOCKER_ACCOUNT: $DOCKER_ACCOUNT"


# -- DOCKER EXEC --
echo ">> BUILDING THE IMAGE ..."
docker build -t $APP_NAME-$SLUG-server .
echo ">> TAGGING THE IMAGE ..."
docker tag $APP_NAME-$SLUG-server $DOCKER_ACCOUNT/$APP_NAME-$SLUG-server:$APP_VERSION
echo ">> PUSHING THE IMAGE TO DOCKER HUB ..."
docker push $DOCKER_ACCOUNT/$APP_NAME-$SLUG-server:$APP_VERSION
echo "\n\n RUN AND EXPOSING THE POD ON PORT: $LOCAL_PORT"
docker run --name $APP_NAME-$SLUG-server -d -p $LOCAL_PORT:$DOCKER_PORT $DOCKER_ACCOUNT/$APP_NAME-$SLUG-server:$APP_VERSION