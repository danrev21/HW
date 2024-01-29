
sudo usermod -aG docker username
su - username

docker login -u docker-registry-username
docker push dtyuev/mynginx:tagname

sudo docker search image-name

# Building images
docker build -t color/green:1.0 .
docker build -t color/blue:2.6 -f Dockerfile_blue .   # -f option when custom dir or name of Dockerfile

# Working with Images
Lifecycle
docker images   - shows all images
docker import   - creates an image from a tarball
docker build    - creates image from Dockerfile
docker build --build-arg CENTOS_IMAGE=centos:8 -t c8j11 .
docker commit   - creates image from a container, pausing it temporarily if it is running
docker rmi      - removes an image
docker image rm centos:8
docker image rm 014e5efa5ca9
docker image prune   - removes "unknown" images
docker load     - loads an image from a tar archive as STDIN, including images and tags
docker save     - saves an image to a tar archive stream to STDOUT with all parent layers, tags & versions
docker tag nginx:latest nginx:new                 # create image copy but new tag
docker tag 0e5574283393 fedora/httpd:version1.0   # the same
           
Info
docker history - shows history of image;
docker tag - tags an image to a name (local or registry).

# Running Contianers
docker run --user 1000:0 jenkins id
docker run --group-add 123 jenkins id
docker run --workdir /var/jenkins_home jenkins pwd
docker run -it -e MYVAR="My Variable" centos env | grep MYVAR
docker run -d --label app=web1 nginx
docker run -d myhttpd:1.0
docker run -P -d myhttpd:1.0    #work if specifyed EXPOSE in Dockerfile
docker run -d -p 8081:80 --name h8081 myhttpd:1.0
docker run -d --restart=always --name sleeper centos sleep 5
docker run -d --restart=unless-stopped --name sleeper centos sleep 5
docker run centos cat /etc/redhat-release
docker run -it centos bash
docker run -dit centos
docker run -dit busybox
docker run -d -p 80:80 -v /usr/share/nginx/html nginx
docker run -d -p 80:80 -v nginx_data:/usr/share/nginx/html nginx
docker run -d --name html_data -v /usr/share/nginx/html busybox sleep infinity
docker run -d -w /data --user 1000:550 --group-add 1200 --env STUDENT=dtyuev --name box busybox sleep infinity
docker run --rm -d \
    --name=tomcat-man \
    --health-cmd="curl http://localhost:8080/_cluster/health || exit 1" \
    --health-interval=2s \
    --health-retries=1 \
    --health-timeout=2s \
    tomcat:8.5.0
docker run -d --volumes-from html_data -p 81:80 nginx

# example docker run:
docker run -it \
    -v /tasks/6/java-app/:/tasks/6/java-app/ \
    -w /tasks/6/java-app/ \
    maven:3.6-jdk-8-alpine \
    mvn clean package
here:
-it - for run it in interactive mode with tty session - for example, to be able to interrupt this script by ^C
-v /tasks/6/java-app/:/tasks/6/java-app/ - for passing our current directory inside the container (so called “bind mount”)
-w /tasks/6/java-app/ - setting “current” working dir to nearly mounted folder - aka “cd $(pwd)”
mvn clean package - command to be executed in the container

alias mvn='docker run -it -v $(pwd):$(pwd) -w $(pwd) maven:3.6-jdk-8-alpine mvn'   

docker exec -it test ps waux

# Stopping and Removing Contianers
docker ps     # shows running containers
docker ps -a  # shows all containers - running and stopped
docker stop h8082
docker container tomcat-man stop
docker rm 014e5efa5ca9
docker container prune       # remove all stopped containers
docker rm $(docker stop $(docker ps -a -q))   # remove all containers
docker ps -qa | xargs -r docker rm
docker ps --format "table {{.Names}}\t{{.ID}}\t{{.Status}}" -f name=tomcat-man

# Working with Network
docker network connect - Connect a container to a network
docker network create - Create a network
docker network disconnect - Disconnect a container from a network
docker network inspect - Display detailed information on one or more networks
docker network ls - List networks
docker network prune - Remove all unused networks
docker network rm - Remove one or more networks
docker info | grep Network

# Working with logs
docker logs container_name 
docker logs container_id
docker logs -f …
docker run -dt --log-driver=journald --name httpd httpd
journalctl -ab CONTAINER_NAME=httpd

docker inspect nginx:latest | jq -r '.[].RootFS'               # number of layers
docker inspect ubuntu:19.10 | jq -r '.[].GraphDriver.Name'     # name of GraphDriver
docker inspect busybox:latest | jq -r '.[].Size'               # size in bytes
docker inspect tomcat-man | jq -r '.[].State.Health'
docker inspect tomcat-man | jq '.[].ContainerConfig.ExposedPorts'
docker inspect tomcat-man | jq '.[].ContainerConfig.Hostname'
docker inspect contbox | jq '.[].Config.Labels'
docker inspect contbox | jq '.[].NetworkSettings.Ports'
docker inspect contbox | jq '.[].NetworkSettings.Networks'  #all except port
docker inspect contbox | jq '.[].NetworkSettings.IPAddress'  #separate data
docker inspect contbox | jq '.[].NetworkSettings.IPPrefixLen' (.Gateway' .MacAddress')

docker ps --format "table {{.Names}}\t{{.ID}}\t{{.Status}}" -f name=tomcat-man
docker image ls --format="{{.Repository}}:{{.Tag}}\t{{.Size}}" | grep nginx


docker volume create --name http-custom-data
docker volume ls
docker volume inspect http-custom-data

docker commit c3f279d17e0a  svendowideit/testimage:version3
docker commit --change='CMD ["apachectl", "-DFOREGROUND"]' -c "EXPOSE 80" c3f279d17e0a  svendowideit/testimage:version4
docker commit --change "ENV DEBUG=true" c3f279d17e0a  svendowideit/testimage:version3

--------
Docker-Compose commands
docker-compose up -d 
docker-compose ps 
docker-compose exec mariadb mysqladmin -p password version 
docker-compose images 
docker-compose logs mariadb 
docker-compose restart mariadb 
docker-compose stop mariadb 
docker-compose down docker-compose down --volumes 
docker-compose build docker-compose up -d 
docker-compose up -d --build 
docker-compose up -d --no-build 
docker-compose up -d --no-cache 

