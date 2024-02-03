
UBUNTU - /var/www/html/index.html
CENTOS ALPINE - /usr/share/nginx/html/index.html





FROM nginx
EXPOSE 80
RUN echo "<html><head></head><body style='background-color:green;'><div style='text-align:center; color: white;'><h1>Green</h1></div></body></html>" > /usr/share/nginx/html/index.html
CMD nginx -g 'daemon off;'

===========================================================================================
ПРОСТО ПРИМЕР (НЕ ТАСК)

FROM nginx
EXPOSE 80
CMD echo "<head></head><body style=\"background-color:green;\"></body>">/usr/share/nginx/html/index.html && nginx -g 'daemon off;'

===============================================================================================

FROM nginx
EXPOSE 80
COPY index_blue.html /usr/share/nginx/html/index.html
CMD nginx -g 'daemon off;'

===============================================================================================

FROM centos:7
LABEL AUTHOR=dtyuev
RUN yum install -y httpd && \
    yum clean all
COPY index.html /var/www/html/
EXPOSE 80
CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]

<html>
  <head>
  </head>
  <body style="background-color:green;">
    <div style='text-align:center; color: white;'>
      <h1>Student: Daniil Tyuev</h1>
    </div>
  </body>
<html>

docker build -t myweb:0.1 .
docker run -d -p 10083:80 myweb:0.1 

===============================================================================================
docker tag myweb:0.1 dtyuev/httpd:1.0
docker images
REPOSITORY     TAG       IMAGE ID       CREATED          SIZE
dtyuev/httpd   1.0       ec63040904a0   12 minutes ago   261MB
myweb          0.1       ec63040904a0   12 minutes ago   261MB
Both images have the same ID's
===============================================================================================
ARGUMENTS                                                                            ARGUMENTS

TASK

ARG CENTOS_IMAGE      # FOR CENTOS:8
FROM ${CENTOS_IMAGE}
ARG JAVA_VERSION=11
RUN curl http://mirror.centos.org/centos/8-stream/BaseOS/x86_64/os/Packages/centos-gpg-keys-8-3.el8.noarch.rpm -o /tmp/centos-gpg-keys-8-3.el8.noarch.rpm && \
    yes | rpm -i /tmp/centos-gpg-keys-8-3.el8.noarch.rpm && \
    dnf -y --disablerepo '*' --enablerepo=extras swap centos-linux-repos centos-stream-repos && \
    yum update -y && \
    yum install -y java-${JAVA_VERSION}-openjdk
CMD /bin/bash

ARG CENTOS_IMAGE       # FOR CENTOS:7
FROM ${CENTOS_IMAGE}
ARG JAVA_VERSION=11
RUN yum update -y && \
    yum install -y java-${JAVA_VERSION}-openjdk
CMD /bin/bash

docker build --build-arg CENTOS_IMAGE=centos:8 -t c8j11 .
docker build --build-arg CENTOS_IMAGE=centos:7 -t c7j180 .

docker run --rm c8j11 java -version 
docker run --rm c7j180 java -version
===============================================================================================
TASK

FROM busybox
WORKDIR /data
COPY test_file1 /data
ADD test_arch.tar /data       #extract into data
ENV MAINTAINER=Daniil_Tyuev

docker build -t dtyuev/mybox .

===============================================================================================
TASK

FROM alpine
RUN apk add figlet
CMD figlet hello world   # or CMD ["figlet", "hello", "world"]
docker build -t dtyuev/figlet:1 .
docker run dtyuev/figlet:1
 _          _ _                            _     _ 
| |__   ___| | | ___   __      _____  _ __| | __| |
| '_ \ / _ \ | |/ _ \  \ \ /\ / / _ \| '__| |/ _` |
| | | |  __/ | | (_) |  \ V  V / (_) | |  | | (_| |
|_| |_|\___|_|_|\___/    \_/\_/ \___/|_|  |_|\__,_|
docker run dtyuev/figlet:1 figlet 'hi there!'
docker run dtyuev/figlet:1 figlet -f script 'hi there!'

===============================================================================================
=TASK=

FROM alpine
RUN apk add figlet
ENTRYPOINT ["figlet", "-f", "mini"]
CMD ["hello", "world"]
docker build -t dtyuev/figlet:3 .
docker run dtyuev/figlet:3
                        
|_  _ || _       _ ._| _| 
| |(/_||(_) \/\/(_)| |(_| 
docker run dtyuev/figlet:3 hi there

|_ o  _|_|_  _ .__  
| ||   |_| |(/_|(/_ 
docker run dtyuev/figlet:3 -f slant hi there
    __    _    __  __                 
   / /_  (_)  / /_/ /_  ___  ________ 
  / __ \/ /  / __/ __ \/ _ \/ ___/ _ \
 / / / / /  / /_/ / / /  __/ /  /  __/
/_/ /_/_/   \__/_/ /_/\___/_/   \___/ 

===============================================================================================
=TASK=

FROM alpine
RUN apk add figlet
ENTRYPOINT ["figlet", "-f", "smslant"]
CMD hello world
docker build -t dtyuev/figlet:4 .
docker run dtyuev/figlet:4
    ___     _          __   _                    _          _ _       
   / / |__ (_)_ __    / /__| |__           ___  | |__   ___| | | ___  
  / /| '_ \| | '_ \  / / __| '_ \   _____ / __| | '_ \ / _ \ | |/ _ \ 
 / / | |_) | | | | |/ /\__ \ | | | |_____| (__  | | | |  __/ | | (_) |
/_/  |_.__/|_|_| |_/_/ |___/_| |_|        \___| |_| |_|\___|_|_|\___/ 
                                                                      
                    _     _ 
__      _____  _ __| | __| |
\ \ /\ / / _ \| '__| |/ _` |
 \ V  V / (_) | |  | | (_| |
  \_/\_/ \___/|_|  |_|\__,_|
docker run dtyuev/figlet:4 hi there
 _     _   _   _                   
| |__ (_) | |_| |__   ___ _ __ ___ 
| '_ \| | | __| '_ \ / _ \ '__/ _ \
| | | | | | |_| | | |  __/ | |  __/
|_| |_|_|  \__|_| |_|\___|_|  \___|

===============================================================================================
=TASK=

FROM alpine
ENV VERSION=v1.2.3
CMD echo VERSION=$VERSION
docker build -t dtyuev/figlet:5-shell -f Dockerfile-shell .

FROM alpine
ENV VERSION=v1.2.3
CMD ["echo", "VERSION=$VERSION"]
docker build -t dtyuev/figlet:5-exec -f Dockerfile-exec .

docker run dtyuev/figlet:5-shell
VERSION=v1.2.3
docker run -e VERSION=v2.3.4 dtyuev/figlet:5-shell
VERSION=v2.3.4
docker run dtyuev/figlet:5-exec
VERSION=$VERSION
docker run -e VERSION=v2.3.4 dtyuev/figlet:5-exec
VERSION=$VERSION

# change into Dockerfile-exec CMD as:
CMD ["/bin/sh", "-c", "echo VERSION=$VERSION"]  

===============================================================================================
===============================================================================================
MULTI-STAGE                                                                         MULTI-STAGE

ONE-STAGE IMAGE

FROM maven:3.6-jdk-8-alpine
WORKDIR /app
COPY pom.xml .
RUN mvn -e -B dependency:resolve
COPY src ./src
RUN mvn -e -B package
CMD ["java", "-jar", "target/jb-hello-world-maven-0.1.0.jar"]

docker build -t one_stage_app -f one_stage_app.Dockerfile .
--------------------------------------------------------------------------------
TWO-STAGE IMAGE

FROM maven:3.6-jdk-8-alpine as builder
WORKDIR /app
COPY pom.xml .
RUN mvn -e -B dependency:resolve
COPY src ./src
RUN mvn -e -B package

FROM openjdk:8-jre-alpine
COPY --from=builder /app .
CMD ["java", "-jar", "target/jb-hello-world-maven-0.1.0.jar"]

docker build -t two_stage_app -f two_stage_app.Dockerfile .
docker run one_stage_app
docker run two_stage_app
docker image ls | grep _stage_app

--------------------------------------------------------------------------------
# it-station-lab такое же задание, только версия проекта в pom.xml 0.2.0 и 
# в команде запуска флаг -ср указывает на запуск класса hello.HelloWorld
FROM maven:3.6-jdk-8-alpine as builder
WORKDIR /app
COPY pom.xml .
RUN mvn -e -B dependency:resolve
COPY src ./src
RUN mvn -e -B package
ENTRYPOINT ["java", "-cp", "target/jb-hello-world-maven-0.2.0.jar"]
CMD ["hello.HelloWorld"]                              
----------------
FROM maven:3.6-jdk-8-alpine as builder
WORKDIR /app
COPY pom.xml .
RUN mvn -e -B dependency:resolve
COPY src ./src
RUN mvn -e -B package

FROM openjdk:8-jre-alpine
COPY --from=builder /app .
ENTRYPOINT ["java", "-cp", "target/jb-hello-world-maven-0.2.0.jar"]
CMD ["hello.HelloWorld"] 

docker image ls | grep javaapp_
javaapp_twostage    latest    cd53bb13f78b   37 seconds ago   85.5MB
javaapp_onestage    latest    19aa995b1b7e   50 minutes ago   141MB
===============================================================================================
ONE-STAGE IMAGE

FROM golang
ENV GOOS=linux
ENV GOARCH=386 
COPY web.go .
## Compiling *.go file
RUN go build -a ./web.go
## Define container process
CMD ["./web"]

docker build -t go_simple -f go_simple.Dockerfile .
docker run -d -p 10089:8080 --name=go_simple go_simple

############ web.go ###################
package main

import (
    "fmt"
    "log"
    "net/http"
    "os"
    "net"
)

func handler(w http.ResponseWriter, r *http.Request) {
    ip, port, _ := net.SplitHostPort(r.RemoteAddr)
    log.Printf("Getting request from %s:%s", ip, port)
    
    hostname, _  := os.Hostname()
    ipaddress, _ := net.LookupHost(hostname)

    fmt.Fprintf(w, "hostname: %s\nip address: %s\n", hostname, ipaddress[0])
}

func main() {
    http.HandleFunc("/", handler)
    log.Fatal(http.ListenAndServe(":8080", nil))
}

###############################################
root@docker-host /data/go $ curl localhost:10089
hostname: 1e31ecc37fa4
ip address: 172.18.0.2
root@docker-host /data/go $ curl localhost:10089
hostname: 1e31ecc37fa4
ip address: 172.18.0.2
root@docker-host /data/go $ curl localhost:10089
hostname: 1e31ecc37fa4
ip address: 172.18.0.2
root@docker-host /data/go $ docker logs go_simple
2021/12/26 12:24:26 Getting request from 172.18.0.1:57964
2021/12/26 12:28:00 Getting request from 172.18.0.1:60578
2021/12/26 12:28:17 Getting request from 172.18.0.1:60786

===============================================================================================
TWO-STAGE IMAGE

FROM golang AS builder
ENV GOOS=linux
ENV GOARCH=386
WORKDIR /data/go/
COPY web.go .
## Compiling *.go file
RUN go build -a ./web.go

FROM scratch
WORKDIR /root/
COPY --from=builder /data/go/web .
EXPOSE 8080

CMD ["./web"]

docker build -t go_multi -f go_multi.Dockerfile .
docker run -d -p 10090:8080 --name=go_multi go_multi

docker images | grep ^go_
go_multi        latest             6d4e6ad11f89   13 seconds ago      5.47MB
go_simple       latest             36db14622d00   3 hours ago         992MB

===============================================================================================
NGINX / CENTOS:7

FROM centos:7
RUN yum install -y epel-release && \
    yum update -y && \
    yum install -y nginx && \
    yum clean all
COPY index.html /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

##check location index.html
docker run -it centos:7 bash 
     
<!DOCTYPE html>
<html>
 <body>
  daniiltyuev/nginx:1-centos
 </body>
</html>
         
docker build -t daniiltyuev/nginx:1-centos .
docker run --name nginx-centos-1 -d -p 10091:80 daniiltyuev/nginx:1-centos

docker push daniiltyuev/nginx:1-centos
docker pull daniiltyuev/nginx:1-centos

===============================================================================================
NGINX / UBUNTU

FROM ubuntu
RUN apt update && \
    apt install -y nginx && \
    apt clean
COPY index.html /var/www/html/index.html
EXPOSE 80
CMD nginx -g 'daemon off;'

<!DOCTYPE html>
<html>
 <body>
  daniiltyuev/nginx:2-ubuntu
 </body>
</html>

docker run -it ubuntu bash ##check location index.html

docker build -t daniiltyuev/nginx:2-ubuntu .
docker run --name nginx-ubuntu-2 -d -p 10092:80 daniiltyuev/nginx:2-ubuntu
push stop rm rmi pull run

===============================================================================================
NGINX / ALPINE

FROM alpine
RUN apk update && \
    apk add nginx && \
    apk cache clean
COPY index.html /usr/share/nginx/html/
COPY nginx.conf /etc/nginx/
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]


docker run -it alpine ##check location index.html
--------------------   
<!DOCTYPE html>
<html>
 <body>
  daniiltyuev/nginx:3-alpine
 </body>
</html>

---- config file nginx ------------------------------------

# Запускать в качестве менее привилегированного пользователя по соображениям безопасности..
user nginx;

# Значение auto устанавливает число максимально доступных ядер CPU,
# чтобы обеспечить лучшую производительность.

worker_processes    auto;

events { worker_connections 1024; }

http {
    server {
        # Hide nginx version information.
        server_tokens off;

        listen  80;
        root    /usr/share/nginx/html;
        include /etc/nginx/mime.types;

        location / {
            try_files $uri $uri/ /index.html;
        }

        gzip            on;
        gzip_vary       on;
        gzip_http_version  1.0;
        gzip_comp_level 5;
        gzip_types
                        application/atom+xml
                        application/javascript
                        application/json
                        application/rss+xml
                        application/vnd.ms-fontobject
                        application/x-font-ttf
                        application/x-web-app-manifest+json
                        application/xhtml+xml
                        application/xml
                        font/opentype
                        image/svg+xml
                        image/x-icon
                        text/css
                        text/plain
                        text/x-component;
        gzip_proxied    no-cache no-store private expired auth;
        gzip_min_length 256;
        gunzip          on;
    }
}
--------------------------------------------------        
docker build -t daniiltyuev/nginx:3-alpine .
docker run --name nginx-alpine-3 -d -p 10093:80 daniiltyuev/nginx:3-alpine

docker push daniiltyuev/nginx:3-alpine
docker pull daniiltyuev/nginx:3-alpine

===============================================================================================
ПРОСТО КОМАНДЫ (НЕ ТАСК)

docker stop nginx-alpine-3
docker rm nginx-alpine-3
docker rmi daniiltyuev/nginx:3-alpine

UBUNTU - /var/www/html/index.html
CENTOS ALPINE - /usr/share/nginx/html/index.html

===============================================================================================
===============================================================================================
TOMCAT / CENTOS

# to know how starts tomcat:
cat /lib/systemd/system/tomcat.service 
[Unit]
Description=Apache Tomcat Web Application Container
After=syslog.target network.target

[Service]
Type=simple
EnvironmentFile=/etc/tomcat/tomcat.conf
Environment="NAME="
EnvironmentFile=-/etc/sysconfig/tomcat
ExecStart=/usr/libexec/tomcat/server start
SuccessExitStatus=143
User=tomcat

[Install]
WantedBy=multi-user.target
---

FROM centos:7
RUN yum -y install tomcat
RUN yum -y install tomcat-webapps
RUN yum -y update
EXPOSE 8080
ENTRYPOINT ["/usr/libexec/tomcat/server"]
CMD ["start"]

docker build -t daniiltyuev/tomcat:5-centos .
docker run -d --name tomcat-centos-5 -p 10095:8080 \
  daniiltyuev/tomcat:5-centos

docker push daniiltyuev/tomcat:5-centos
docker pull daniiltyuev/tomcat:5-centos

docker stop tomcat-centos-5
docker rm tomcat-centos-5
docker rmi daniiltyuev/tomcat:5-centos

===============================================================================================
TOMCAT / UBUNTU


# to know how starts tomcat:
cat /lib/systemd/system/tomcat9.service 

[Unit]
Description=Apache Tomcat 9 Web Application Server
Documentation=https://tomcat.apache.org/tomcat-9.0-doc/index.html
After=network.target
RequiresMountsFor=/var/log/tomcat9 /var/lib/tomcat9

[Service]

# Configuration
Environment="CATALINA_HOME=/usr/share/tomcat9"                       <------- 
Environment="CATALINA_BASE=/var/lib/tomcat9"                         <-------    
Environment="CATALINA_TMPDIR=/tmp"                                   <-------    these strings add into the
                                                                                        Dockerfile
Environment="JAVA_OPTS=-Djava.awt.headless=true"                     <-------

# Lifecycle
Type=simple
ExecStartPre=+/usr/libexec/tomcat9/tomcat-update-policy.sh           <-------   these strings all add into the
                                                                                        Dockerfile
ExecStart=/bin/sh /usr/libexec/tomcat9/tomcat-start.sh               <-------
SuccessExitStatus=143
Restart=on-abort

# Logging
SyslogIdentifier=tomcat9

# Security
User=tomcat
Group=tomcat
PrivateTmp=yes
AmbientCapabilities=CAP_NET_BIND_SERVICE
NoNewPrivileges=true
CacheDirectory=tomcat9
CacheDirectoryMode=750
ProtectSystem=strict
ReadWritePaths=/etc/tomcat9/Catalina/
ReadWritePaths=/var/lib/tomcat9/webapps/
ReadWritePaths=/var/log/tomcat9/

[Install]
WantedBy=multi-user.target
---
FROM ubuntu
RUN apt-get update -y && \
    apt-get install -y tomcat9 && \
    apt clean
ENV CATALINA_HOME=/usr/share/tomcat9
ENV CATALINA_BASE=/var/lib/tomcat9
ENV CATALINA_TMPDIR=/tmp
ENV JAVA_OPTS=-Djava.awt.headless=true
EXPOSE 8080
RUN /usr/libexec/tomcat9/tomcat-update-policy.sh
CMD /bin/sh /usr/libexec/tomcat9/tomcat-start.sh
---

# one more approach:
FROM ubuntu
RUN apt -y update && \
    apt -y install wget && \
    apt -y install tar && \
    apt -y install default-jdk && \
    apt-get clean
ENV CATALINA_HOME /opt/tomcat
ENV TOMCAT_MAJOR 9
ENV TOMCAT_VERSION 9.0.85
RUN wget https://dlcdn.apache.org/tomcat/tomcat-${TOMCAT_MAJOR}/v${TOMCAT_VERSION}/bin/apache-tomcat-${TOMCAT_VERSION}.tar.gz && \
    tar -xvf apache-tomcat-${TOMCAT_VERSION}.tar.gz && \
    rm apache-tomcat*.tar.gz && \
    mv apache-tomcat* ${CATALINA_HOME}
RUN chmod +x ${CATALINA_HOME}/bin/*sh
EXPOSE 8080
CMD ["opt/tomcat/bin/catalina.sh", "run"]
---
docker build -t daniiltyuev/tomcat:6-ubuntu .
docker run -d --name tomcat-ubuntu-6 -p 10096:8080 \
  daniiltyuev/tomcat:6-ubuntu

docker stop tomcat-ubuntu-6
docker rm tomcat-ubuntu-6
docker rmi daniiltyuev/tomcat:6-ubuntu

===============================================================================================
TOMCAT / ALPINE

запускаем контейнер на альпине и устанавливаем туда руками java, tomcat и создаем исходя из этого докерфайл:

FROM alpine
RUN apk update && apk upgrade && \
    apk add wget tar openjdk8-jre-base && \
    apk cache clean
RUN mkdir /opt/tomcat
ENV CATALINA_HOME /opt/tomcat
ENV CATALINA_BASE /opt/tomcat
RUN wget https://dlcdn.apache.org/tomcat/tomcat-9/v9.0.85/bin/apache-tomcat-9.0.85.tar.gz && \
    tar xvzf apache-tomcat-9.0.85.tar.gz --strip-components 1 --directory /opt/tomcat && \
    rm apache-tomcat*.tar.gz
EXPOSE 8080
CMD ["opt/tomcat/bin/catalina.sh", "run"]

# one more approach:
FROM alpine
RUN apk -U upgrade --update && \
    apk add curl && \
    apk add wget && \
    apk add tar && \
    apk add openjdk8-jre-base
ENV CATALINA_HOME /opt/tomcat
ENV TOMCAT_MAJOR 9
ENV TOMCAT_VERSION 9.0.56
RUN wget https://dlcdn.apache.org/tomcat/tomcat-${TOMCAT_MAJOR}/v${TOMCAT_VERSION}/bin/apache-tomcat-${TOMCAT_VERSION}.tar.gz && \
    tar -xvf apache-tomcat-${TOMCAT_VERSION}.tar.gz && \
    rm apache-tomcat*.tar.gz && \
    mv apache-tomcat* ${CATALINA_HOME}
RUN chmod +x ${CATALINA_HOME}/bin/*sh
EXPOSE 8080
CMD ["opt/tomcat/bin/catalina.sh", "run"]

docker build -t daniiltyuev/tomcat:7-alpine .
docker run -d --name tomcat-alpine-7 -p 10097:8080 \
  daniiltyuev/tomcat:7-alpine

docker stop tomcat-alpine-7
docker rm tomcat-alpine-7
docker rmi daniiltyuev/tomcat:7-alpine

###check
$ curl -sL -w "HTTP Response: %{http_code}\n" 0.0.0.0:10097 -o/dev/null
HTTP Response: 200

$ curl -s localhost:10097 | grep '.title.Apache Tomcat.*'
        <title>Apache Tomcat/9.0.37</title>


docker image ls --format="{{.Repository}}:{{.Tag}}\t{{.Size}}" | grep tomcat
===============================================================================================
ПРОСТО ПРИМЕР (НЕ ТАСК)

##download sample.war
FROM tomcat:8.5.35-jre10
ADD sample.war /usr/local/tomcat/webapps/
EXPOSE 8080
CMD chmod +x /usr/local/tomcat/bin/catalina.sh
CMD ["catalina.sh", "run"]

===============================================================================================
===============================================================================================
DOCKER CONTAINERS                                                             DOCKER CONTAINERS
  
FROM nginx
EXPOSE 80
CMD echo "<head></head><body style=\"background-color:green;\"></body>">/usr/share/nginx/html/index.html && nginx -g 'daemon off;'  
docker build -t color/green:1.0 .
docker run -d color/green:1.0 
docker ps

===============================================================================================
docker run -d -p 12025:80 --name my-container color/green:1.0
docker port my-container 
80/tcp -> 0.0.0.0:12025
docker inspect my-container | jq '.[].NetworkSettings.Ports'

===============================================================================================
docker run -d -p 10084:80 --name my-container-2 color/green:1.0
99107be2b0c0a168714ed2ac59175c83a0e2d1fa5bc0456dec9474f817a436b0
root@docker-host /data $ docker inspect my-container-2 | jq '.[].NetworkSettings.Ports'
{
  "80/tcp": [
    {
      "HostIp": "0.0.0.0",
      "HostPort": "10084"
    }
  ]
}

===============================================================================================
# restart regardless of the exit status
docker run -d --name=restarter_1 --restart=always busybox sleep 3
# restart only if the container exits with a non-zero exit status
docker run -d --name=restarter_2 --restart=on-failure:7 busybox sleep -3
docker ps --format "table {{.ID}}\t{{.Names}}\t{{.Status}}"

===============================================================================================
docker run -d --restart always --name <cont> <image>
docker run -d --restart always --name restarter_1 busybox sleep 3 ########
docker rm --force restarter_1

===============================================================================================
# Using image busybox:1.28 run a command nslookup google.com. Save its output to /var/log/nslookup_google.com on the Host’s system.
docker run --rm busybox:1.28 nslookup google.com > /var/log/nslookup_google.com

===============================================================================================

docker run -d --name batman nginx
docker exec batman mkdir data
docker exec batman touch /data/student
docker exec batman ls /data/
docker exec -it batman bash
echo "Daniil Tyuev" > student
cat student
docker exec batman cat /data/student
===============================================================================================
docker stop batman
docker rm -f restarter_1 

===============================================================================================
docker run -d -w /data --user 1000:550 --group-add 1200 --env STUDENT=dtyuev --name box busybox sleep infinity

$ docker exec -it box sh
/data $ id
uid=1000 gid=550 groups=1200
/data $ echo $STUDENT
dtyuev
/data $ ps -ef
PID   USER     TIME  COMMAND
    1 1000      0:00 sleep infinity
    6 1000      0:00 sh
   13 1000      0:00 ps -ef
/data $ exit

===============================================================================================
containers / 10

docker run --rm -d --name=tomcat-man --health-cmd="curl --silent --fail localhost:8080 || exit 1" --health-interval=5s --health-retries=5 --health-timeout=2s tomcat:8.5.0
docker ps --format "table {{.Names}}\t{{.ID}}\t{{.Status}}" -f name=tomcat-man
docker inspect tomcat-man | jq -r '.[].State.Health'

===============================================================================================
containers / 11

docker run -d -p 10091:80 --name nginx_wrong nginx:alpine
docker logs nginx_wrong  =отсюда узнаем про -1024
docker inspect nginx_wrong   =отсюда определяем биндинг (mounts)
     /tmp/index.html:/usr/share/nginx/html/index.html
     /var/nginx/nginx.conf:/etc/nginx/nginx.conf

на хосте исправить конф (убрать - перед 1024 из задания)
vim /var/nginx/nginx.conf
docker restart nginx_wrong
либо
docker run -d -p 10091:80 -v /tmp/index.html:/usr/share/nginx/html/index.html -v /var/nginx/nginx.conf:/etc/nginx/nginx.conf --name nginx_wrong nginx:alpine

===============================================================================================
containers / 12

docker run -d -p 10092:80 --log-driver=journald --name nginx_journal nginx 
curl localhost:10092
journalctl -ab CONTAINER_NAME=nginx_journal

===============================================================================================
containers / 13      quiz 1 2 3 4 1 3 1

===============================================================================================
===============================================================================================
VOLUMES                                                                                 VOLUMES

Working with Volumes
docker volume create - Create a volume;
docker volume inspect - Display detailed information on one or more volumes;
docker volume ls - List volumes;
docker volume prune - Remove all unused local volumes;
docker volume rm - Remove one or more volumes

===============================================================================================
docker volume inspect volume-1 | jq '.[].Mountpoint'
docker volume inspect volume-2 | jq '.[].Options.device'
docker volume inspect volume-1 | jq '.[].Mountpoint'
docker volume inspect volume-3 | jq '.[].Options.type'
docker volume inspect volume-3 | jq '.[].Options.device'

===============================================================================================
VOLUMES / 2

docker run -d -p 10082:80 -v /opt/index.html:/usr/share/nginx/html/index.html --name c10082 nginx

===============================================================================================
VOLUMES / 3

docker run -d -p 10083:80 -v /usr/share/nginx/html --name c10083 nginx
docker inspect c10083 | jq '.[].Mounts[].Source'
ls -lah /var/lib/docker/volumes/c148792b3891a97254387153acbdc0e75644331412de41bab5be60a108306b1c/_data
echo 'This is c10083 container' > var/lib/docker/volumes/c148792b3891a97254387153acbdc0e75644331412de41bab5be60a108306b1c/_data/index.html

===============================================================================================
VOLUMES / 4

docker run -d -p 10084:80 -v c10084_data:/usr/share/nginx/html --name c10084 nginx
docker inspect c10084 | jq '.[].Mounts[].Source'
ls -lah /var/lib/docker/volumes/c10084_data/_data
echo 'This is the c10084 container' > /var/lib/docker/volumes/c10084_data/_data/index.html

===============================================================================================
VOLUMES / 5

docker run -itd -v /root/index.html:/usr/share/nginx/html/index.html --name html_data busybox
docker run -d -p 10085:80 --volumes-from html_data --name=c10085 nginx
docker run -d -p 10086:80 --volumes-from html_data --name=c10086 nginx

===============================================================================================
VOLUMES / 6

docker volume create c10087_custom_volume
docker inspect c10087_custom_volume
docker volume inspect c10087_custom_volume | jq '.[].Mountpoint'
cd /var/lib/docker/volumes/c10087_custom_volume/_data
echo "My custom docker volume with name c10087_custom_volume" > index.html
docker run -d -p 10087:80 -v c10087_custom_volume:/usr/share/nginx/html --name c10087 nginx 

docker inspect --format='{{.HostConfig.Binds}}' c10087
docker inspect c10087 | jq '.[].Mounts'

===============================================================================================
VOLUMES / 7  quiz   2 1 1 3 3 

===============================================================================================
===============================================================================================
DOCKER NETWORKS                                                                 DOCKER NETWORKS

1
docker network ls
docker network inspect
docker network inspect bridge | grep masq*
docker network inspect my_custom_network_1 | jq '.[].Driver'
docker network inspect my_custom_network_2 | jq '.[].IPAM.Config[].Subnet'
docker network inspect my_custom_network_1 | grep mtu*
docker network inspect my_custom_network_2 | jq '.[].IPAM.Config[].Gateway'

===============================================================================================
2
docker network ls
NETWORK ID     NAME                  DRIVER    SCOPE
8202a2d6095b   bridge                bridge    local
889848feeeab   host                  host      local
d87199772efb   my_custom_network_1   bridge    local
99c97e461c79   my_custom_network_2   bridge    local
f58b4ebdb071   none                  null      local
docker run -d --name httpd_host --network host httpd

===============================================================================================
3
docker run -it -d --network bridge --name alpine_busy alpine
docker run -it -d --network bridge --name busybox_busy busybox
docker network inspect bridge 
[
    {
        "Name": "bridge",
        "Id": "8202a2d6095b6ef751e68ceee9134c22798b0d8ec3612ebcfd9262c5b1f5b7da",
        "Created": "2024-01-30T21:50:52.81271173Z",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": null,
            "Config": [
                {
                    "Subnet": "172.18.0.0/16",
                    "Gateway": "172.18.0.1"
                }
            ]
        },
        "Internal": false,
        "Attachable": false,
        "Ingress": false,
        "ConfigFrom": {
            "Network": ""
        },
        "ConfigOnly": false,
        "Containers": {
            "6e74a4311c44acf5e8d3d4117d6dc22b87ebe7d8c6765584f9ce5ec0b5e9a9c9": {
                "Name": "alpine_busy",
                "EndpointID": "fd0347b16c69a5ba55bcc4bfe3144ee4bcafc8c1aeaf966451c204f129319745",
                "MacAddress": "02:42:ac:12:00:02",
                "IPv4Address": "172.18.0.2/16",
                "IPv6Address": ""
            },
            "fd2cf7defd3690a61ede5b54a5b79431df324b211d467f5d307331e2e9efa48d": {
                "Name": "busybox_busy",
                "EndpointID": "fcace2e5751b2a00650fd588df834a9847f4ae64a7fd1b5479325c052aff7e91",
                "MacAddress": "02:42:ac:12:00:03",
                "IPv4Address": "172.18.0.3/16",
                "IPv6Address": ""
            }
        },
        "Options": {
            "com.docker.network.bridge.default_bridge": "true",
            "com.docker.network.bridge.enable_icc": "true",
            "com.docker.network.bridge.enable_ip_masquerade": "true",
            "com.docker.network.bridge.host_binding_ipv4": "0.0.0.0",
            "com.docker.network.bridge.name": "docker0",
            "com.docker.network.driver.mtu": "1500"
        },
        "Labels": {}
    }
]

===============================================================================================
4
docker network create -d bridge dtyuev-bridge --subnet 123.45.1.0/24 --ip-range 123.45.1.0/24 --label createdby=Daniil_Tyuev
docker network inspect dtyuev-bridge

===============================================================================================
5
docker ps
docker network ls
docker network inspect bridge ---> сеть по умолчанию, понимает только айпишники, поэтому
создаем именованный бридж со своей сетью
docker network create -d bridge net1 --subnet 152.18.0.0/16 --ip-range 152.18.0.0/16 --label createdby=Daniil

присоединяем контейнеры пинг и понг к этому именованому бриджу 
docker network connect net1 --ip 152.18.0.5 pong
docker network connect net1 --ip 152.18.0.4 ping
docker network inspect net1
и они пингуются
docker exec ping ping -c3 pong

===============================================================================================
6
docker network ls
docker network inspect dtyuev-bridge 
docker run -d --network dtyuev-bridge --name nginx-dtyuev-bridge --label createdby=Daniil_Tyuev nginx
docker run -d --network dtyuev-bridge --name tomcat-dtyuev-bridge --label createdby=Daniil_Tyuev tomcat

===============================================================================================
7   quiz 4 1

===============================================================================================
===============================================================================================
NAMESPACES CGROUPS                                                           NAMESPACES CGROUPS 

2
Run busy_sleep_inf container with sleep infinity command in nginx_pid container PID Namespace.
Т.е. что бы увидеь процесс команды sleep infinity запущенной в контейнере busy_sleep_inf  в процессах контейнера nginx_pid:

docker run -d --name nginx_pid nginx:alpine
docker run -d --pid=container:nginx_pid --name busy_sleep_inf busybox sleep infinity
docker exec busy_sleep_inf ps
 PID   USER     TIME  COMMAND
    1 root      0:00 nginx: master process nginx -g daemon off;
   24 101       0:00 nginx: worker process
   25 101       0:00 nginx: worker process
   26 root      0:00 sleep infinity
   34 root      0:00 ps

===============================================================================================
3
# net-tools should run in nginx-net container NET Namespace
docker run -d -t --network=container:nginx-net --name net-tools sbeliakou/net-tools
docker exec nginx-net hostname -i
172.18.0.4
docker exec net-tools hostname -i
172.18.0.4 
===============================================================================================
4
# Create a container and run it in UTS namespace of the Host.
docker run -d --uts=host --name busy-host busybox sleep infinity
root@docker-host ~ $ hostname
docker-host
root@docker-host ~ $ hostname
docker-host

===============================================================================================
5
# container should have 100 Mb memory limit
# container should use unlimited swap
# container should reserve 50 Mb of memory
docker run -d --memory="100m" --memory-swap="-1" --memory-reservation="50m" --name=tomcat tomcat:jdk8-openjdk-slim
docker stats tomcat --no-stream
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT   MEM %     NET I/O   BLOCK I/O   PIDS
4c9aab2d8a17   tomcat    0.35%     50.37MiB / 100MiB   50.37%    0B / 0B   0B / 0B     17

===============================================================================================
6
# command: md5sum /dev/urandom
# container should have 20% CPU limit (use --cpu-quota=20000 option).
# запись --cpus=0.20 и --cpu-period=100000 --cpu-quota=20000 это одно и тоже:

docker run -d --cpu-period=100000 --cpu-quota=20000 --name=cpu-stress alpine md5sum /dev/urandom

docker stats cpu-stress --no-stream 
CONTAINER ID   NAME         CPU %     MEM USAGE / LIMIT   MEM %     NET I/O   BLOCK I/O   PIDS
754c1cb99ad4   cpu-stress   20.06%    756KiB / 3.598GiB   0.02%     0B / 0B   0B / 0B     1
===============================================================================================
===============================================================================================
DOCKER COMPOSE                                                                   DOCKER COMPOSE

2
version: "3"
services:
  web:
    image: nginx:alpine
    environment:
      TZ: Europe/Minsk
    ports:
      - 80:80
      - 443:443
    tmpfs:
      - /run
      - /tmp
      - /var/cache/nginx

docker-compose up -d
2_web_1 is up-to-date
docker-compose ps
 Name                Command               State                               Ports                             
-----------------------------------------------------------------------------------------------------------------
2_web_1   /docker-entrypoint.sh ngin ...   Up      0.0.0.0:443->443/tcp,:::443->443/tcp,                         
                                                   0.0.0.0:80->80/tcp,:::80->80/tcp                              
docker-compose stop
Stopping 2_web_1 ... done

===============================================================================================
3
docker-compose down
===============================================================================================

4
version: "3"
services:
  httpd:
    container_name: httpd_web
    image: httpd
    ports:
      - 10084:80
    environment:
      - COURSE=compose
      - MAINTAINER=dtyuev
    restart: on-failure
===============================================================================================
5
version: "3"
services:
  httpd:
    container_name: nginx_web
    image: nginx:1.16
    ports:
      - 10085:80
      - 50000:50000
    volumes:
      - /task/5/index.html:/usr/share/nginx/html/index.html
    env_file: /task/5/nginx_env
    restart: on-failure
    logging:
      driver: journald
===============================================================================================
6
version: "3"
services:
  web:
    container_name: nginx_task6
    image: nginx:alpine
    ports:
      - 10086:80
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf

  tomcat:
    container_name: tomcat_task6
    image: tomcat:8.0
----------------------------------
#nginx.conf#
events {
    worker_connections 1024;
}

http {
 server {
    listen 80;
    server_name localhost;

    location / {
      proxy_pass http://tomcat:8080;
    }
  }
}
===============================================================================================
7
version: '3'
services:
  pod:
    image: k8s.gcr.io/pause:3.3
    container_name: pause
    ports:
      - 10087:80
  web:
    image: nginx:alpine
    container_name: nginx_task7    
    network_mode: "service:pod"

pod - можно заменить на что угодно (например, pause)
===============================================================================================
8
# этот ямл дан, по нему воссоздать ресурсы

version: '2'
services:
  redis:
    container_name: redis-server
    image: bitnami/redis:5.0
    hostname: redis-server
    environment:
      ALLOW_EMPTY_PASSWORD: "yes"
      REDIS_DISABLE_COMMANDS: FLUSHDB,FLUSHALL
    ports:
      - published: 6379
        target: 6379
    volumes:
      - redis_data:/bitnami/redis/data:rw
    networks:
      - database
volumes:
  redis_data:
    name: redis_data
networks:
  database:
    name: database
----------------------------------
docker volume create redis_data
docker network create database
docker run -d --name redis-server --hostname redis-server --env "ALLOW_EMPTY_PASSWORD=yes" --env "REDIS_DISABLE_COMMANDS=FLUSHDB,FLUSHALL" -p 6379:6379 -v redis_data:/bitnami/redis/data:rw --network database bitnami/redis:5.0

===============================================================================================
9
# у нас есть:
# Dockerfile:
FROM php:7.2-apache
RUN apt-get update
RUN docker-php-ext-install pdo pdo_mysql mysqli
-------------------------------------------------
# yaml file:
services:
  web:
    container_name: web
    hostname: web
    build: 
      context: /task/9/nginx_php
    image: web_locally_build
    environment:
      - ALLOW_OVERRIDE=true
    ports:
      - "10089:80"
    volumes:
      - ./app:/var/www/html/
  db:
    container_name: db
    hostname: db
    image: mysql:5.7
    restart: always
    volumes:
      - ./mysql:/var/lib/mysql
    environment:
      MYSQL_ROOT_PASSWORD: root
      MYSQL_USER: admin
      MYSQL_PASSWORD: test
      MYSQL_DATABASE: database
    ports:
      - "8889:3306"
----------------------------------
# index.php
<?php
$servername = "db";
$username = "admin";
$password = "test";
$dbname = "database";

try {
    $conn = new PDO("mysql:host=$servername;dbname=database", $username, $password);
    // set the PDO error mode to exception
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    echo "Connected successfully. Great work!";
    }
catch(PDOException $e)
    {
    echo "Connection failed: " . $e->getMessage();
    }
?>

-------------------------------
docker build -t web_locally_build .

docker network create nginx_php_default

docker run -d -p 10089:80 -v /task/9/nginx_php/app:/var/www/html/ --network nginx_php_default --hostname web --env "ALLOW_OVERRIDE=true" --name web web_locally_build

docker run -d -p 8889:3306 -v /task/9/nginx_php/mysql:/var/lib/mysql --network nginx_php_default --hostname db --env "MYSQL_ROOT_PASSWORD=root" --env "MYSQL_USER=admin" --env "MYSQL_PASSWORD=test" --env "MYSQL_DATABASE=database" --restart always --name db mysql:5.7

curl dtyuev.devops.edu.playpit.net:10089


docker-compose up -d
docker-compose ps

docker-compose exec mariadb mysqladmin -ppassword version

docker-compose images

docker-compose logs mariadb

docker-compose restart mariadb
docker-compose stop mariadb

docker-compose down
docker-compose down --volumes

docker-compose build
docker-compose up -d
docker-compose up -d --build
docker-compose up -d --no-build
docker-compose up -d --no-cache
===============================================================================================
===============================================================================================
DAEMON                                                                                   DAEMON
1
usermod -aG docker dtyuev
===============================================================================================
2
vim /etc/docker/daemon.json
{
  "log-driver": "syslog",
  "log-opts": {
    "syslog-address": "udp://1.2.3.4:1111"
  }
}
systemctl restart docker
docker info --format '{{.LoggingDriver}}'

===============================================================================================
3
vim /etc/docker/daemon.json
{
  "log-driver": "syslog",
  "debug": true,               ## add this
  "log-opts": {
    "syslog-address": "udp://1.2.3.4:1111"
  }
}
systemctl restart docker
docker info --format '{{.Debug}}'
docker run -dt --name mycontainer busybox
journalctl -u docker | grep mycontainer
===============================================================================================
4
vim /etc/docker/daemon.json
{
  "log-driver": "syslog",
  "debug": true,              ## add this
  "live-restore": true,
  "log-opts": {
    "syslog-address": "udp://1.2.3.4:1111"
  }
}
systemctl restart docker
docker info --format '{{ .LiveRestoreEnabled }}'
docker run -d --net host nginx
docker ps
curl -IL localhost
systemctl stop docker
systemctl status docker
curl -IL localhost
===============================================================================================
5
vim /etc/docker/daemon.json

{
"log-driver": "syslog",
"debug": true,
"live-restore": true,
"hosts": ["tcp://127.0.0.1:2375"]
}

systemctl restart docker
Job for docker.service failed because the control process exited with error code.
See "systemctl status docker.service" and "journalctl -xe" for details.
vim /lib/systemd/system/docker.service
IN
ExecStart=/usr/bin/dockerd --containerd=/run/containerd/containerd.sock
Delete : -H fd://



systemctl daemon-reload
systemctl start docker

===============================================================================================
6

systemctl edit docker.service чтобы открыть файл переопределения для docker.serviceв текстовом редакторе.

Добавьте или измените следующие строки, подставляя свои собственные значения.

[Service]
ExecStart=
ExecStart=/usr/bin/dockerd -H fd:// -H tcp://127.0.0.1:2375
Сохраните файл.

Перезагрузите systemctlконфигурацию.

 sudo systemctl daemon-reload
Перезагрузите Docker.

 sudo systemctl restart docker.service
......







===============================================================================================


























