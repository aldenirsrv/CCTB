ls ms-go/
ls python-ms/
ls frontend/
# chmod 755 ms-go/commands.sh
# chmod 755 python-ms/commands.sh
# chmod 755 frontend/commands.sh

# # Load application variables
# . app-config.sh
# . ms-go/commands.sh
# . python-ms/commands.sh
# . frontend/commands.sh

# # Local variables
SLUG="python|go|frontend"
PORT="5000|8000"
echo "APP_VERSION: $APP_VERSION"
echo "APP_NAME: $APP_NAME"
echo "SLUG: $SLUG"

# echo ">> RUN LOCAL CONTAINER BASED ON DOCKER HUM IMAGE AND EXPOSING IN $PORT ..."
echo "\n\n RUN SUCH COMMANDS TO CHECK YOUR POD"
echo '---[CMD]---'
echo "EXPOSE LOCALLY ON PORT<$PORT> -- change de port -<your_port>:<container_port>"
echo docker run --name $APP_NAME-$SLUG-server -d -p $PORT:5000 aldenir/$APP_NAME-$SLUG-server:$APP_VERSION

echo '\n---[CMD]---'
# echo "LOGGING TO CONTAINER: $APP_NAME-$SLUG-server"
echo "Application logs.. -- use docker logs -f <container-name> to interactive log"
echo  docker logs  $APP_NAME-$SLUG-server # docker logs -f <container-name> to interactive log
echo '\n---[CMD]---'
# docker search $SLUG
echo "Show infra processess..."
echo docker stats $APP_NAME-$SLUG-server
echo "Entering in to the pod..."
echo docker exec -it $APP_VERSION-$SLUG-server bash
# docker stop $APP_VERSION-$SLUG-server


docker logs  $APP_NAME-python-server $APP_NAME-go-server
# docker stats $APP_NAME-python-server $APP_NAME-go-server