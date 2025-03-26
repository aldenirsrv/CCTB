figlet "DOCKER HUB"

echo "\033[32m>> LOCAL IMAGES...\033[0m"
docker image ls | grep financial | grep -v 'aldenir/'

echo "\033[32m>> DOCKER HUB IMAGES...\033[0m"
docker image ls | grep financial | grep 'aldenir/'