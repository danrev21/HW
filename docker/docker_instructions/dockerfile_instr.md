
Dockerfile preferences
-----------------------------------------------------
# .dockerignore 
помогает избежать ненужной отправки больших или конфиденциальных файлов и каталогов демону и возможного добавления их в образы с помощью ADD или COPY
пример:
# comment
*/temp*           - исключаюся /somedir/temporary.txt, /somedir/temp
*/*/temp*         - искл. /somedir/subdir/temporary.txt
temp?             - /tempa, /tempb

знак ! для создания исключений из исключений:
*.md          - искл. OUTPUT.md
!README.md    - исключить все указанное, за исключ. README.md

не включаются в контекст, за исключением файлов README, отличных от README-secret.md (определяет последняя строка):
*.md
!README*.md
README-secret.md    

Все файлы README включены (определяет последняя строка):
*.md
README-secret.md
!README*.md

Можно использовать .dockerignore файл для исключения файлов Dockerfile и .dockerignore. Эти файлы по-прежнему отправляются демону, потому что они нужны ему для выполнения своей работы. Но инструкции ADD и COPY не копируют их в образ.

===================================================================================================================
# Variables
обозначаются Dockerfile либо с помощью $variable_name, либо ${variable_name}

  Синтаксис ${variable_name}также поддерживает несколько стандартных bash модификаторов, как указано ниже:
  ${variable:-word} указывает, что если variable установлено, результатом будет это значение. Если variable не установлено, то word будет результат.
  ${variable:+word} указывает, что если variable установлено, то word будет результатом, иначе результатом будет пустая строка.
  Во всех случаях wordможет быть любой строкой, включая дополнительные переменные среды.

  Пример:
FROM busybox
ENV FOO=/bar
WORKDIR ${FOO}   # WORKDIR /bar
ADD . $FOO       # ADD . /bar
COPY \$FOO /quux # COPY $FOO /quux

  Переменные среды поддерживаются следующим списком инструкций в файле Dockerfile:
ADD
COPY
ENV
EXPOSE
FROM
LABEL
STOPSIGNAL
USER
VOLUME
WORKDIR
ONBUILD (в сочетании с одной из поддерживаемых выше инструкций)

  Подстановка переменных среды будет использовать одно и то же значение для каждой переменной на протяжении всей инструкции. 
  
  Другими словами, в этом примере:
ENV abc=hello
ENV abc=bye def=$abc
ENV ghi=$abc
  приведет к def значению hello, а не bye. Однако ghi будет иметь значение bye поскольку оно не является частью той же инструкции, для которой задано abc значение bye.
  
===================================================================================================================

ADD 
копирует новые файлы, каталоги или URL-адреса удаленных файлов <src> и добавляет их в файловую систему образа по пути <dest>.

COPY
копирует новые файлы или каталоги <src> и добавляет их в файловую систему контейнера по пути <dest>.

Если переменная среды нужна только во время сборки, а не в финальном образе, используйте ARG, который не сохраняется в финальном изображении

Не путайте RUN с CMD. RUN фактически запускает команду и фиксирует результат; CMD ничего не выполняет во время сборки, но указывает предполагаемую команду для образа.

Docker images are read only
Сommand 'docker tag' is used to set which registry an image will be uploaded to.
The command docker pull is used to download images while the command docker pus is used to upload them.
Each line of a docker file makes a new independent image based on the previous line’s image.
The CMD instruction sets the program to run when the container starts in a Docker file.
The Docker file RUN command starts a program that runs only for one line of the Docker file.
The Docker file ENV command set environment variables in the rest of the docker file, and in the finished image.
The Docker file WORKDIR instruction changes directories both for the rest of the docker file, and in the finished image

И ENTRYPOINT, и CMD указывают, какой процесс (просто говоря, команда) должен запускаться в контейнере в качестве основного процесса.

Когда Dockerfile содержит несколько директив CMD, важно отметить, что вступят в силу только инструкции из последнего CMD, что позволяет четко и предсказуемо настроить поведение контейнера по умолчанию.

CMD инструкция будет выполнятся по умолчанию, но если при запуске контейнера указать другой аргумент, то он и поступит на вход ENTRYPOINT.
Если формы отличаются:
  ENTRYPOINT ["echo"] - exec
  CMD hello world     - shell
то по умолчанию вместе с аргументом 'hello world' на вход ENTRYPOINT поступит '/bin/sh -c', и в итоге: /bin/sh -c hello world
А при указании аргумента 'hi there' при запуске контейнера ENTRYPOINT примет только указанный аргумент: hi there

Для обработки переменных - shell либо CMD [ "sh", "-c", "echo $HOME" ]

ENTRYPOINT Инструкция:
Похож на CMD, но основное отличие состоит в том, что он предоставляет исполняемый файл в качестве команды по умолчанию.
В отличие от CMD, команда и ее параметры не игнорируются, когда Docker запускает контейнер с помощью альтернативной команды.
Если файл Dockerfile содержит обе инструкции CMDи ENTRYPOINT, CMDаргументы инструкции добавляются к файлу ENTRYPOINT.

Инструкция CMD:
Используется для предоставления значений по умолчанию для исполняемого контейнера.
Указывает команду и/или параметры по умолчанию, которые будут выполняться при запуске контейнера.
Если a Dockerfile имеет несколько CMD инструкций, вступает в силу только последняя.
Инструкцию CMD можно переопределить во время выполнения, передав аргументы docker run.

Best Practices:
Используйте CMD для установки команды по умолчанию, которую можно легко переопределить.
Используйте ENTRYPOINT для установки основной команды для контейнера. Он часто используется CMD для предоставления аргументов по умолчанию.
Комбинируйте ENTRYPOINT и CMD разумно, чтобы сделать ваш образ более гибким и настраиваемым.
Если вам нужно запустить контейнер как исполняемый файл (например, docker run myimage arg1 arg2), используйте ENTRYPOINT.