===================================================================================================================
# COPY
копирует новые файлы или каталоги <src> и добавляет их в файловую систему контейнера по пути <dest>.
COPY [--chown=<user>:<group>] [--chmod=<perms>] <src>... <dest>
COPY [--chown=<user>:<group>] [--chmod=<perms>] ["<src>",... "<dest>"]
Эта последняя форма требуется для путей, содержащих пробелы.

  Можно указать несколько <src> ресурсов, но пути к файлам и каталогам будут интерпретироваться относительно источника контекста сборки.

COPY hom* /mydir/
COPY hom?.txt /mydir/
COPY test.txt relativeDir/
COPY test.txt /absoluteDir/
  чтобы скопировать файл с именем arr[0].txt:
COPY arr[[]0].txt /mydir/

  Все новые файлы и каталоги создаются с UID и GID, равными 0, если только необязательный --chownфлаг не указывает данное имя пользователя, имя группы или комбинацию UID/GID для запроса конкретного владельца скопированного содержимого.

COPY --chown=55:mygroup files* /somedir/
COPY --chown=bin files* /somedir/
COPY --chown=1 files* /somedir/
COPY --chown=10:11 files* /somedir/
COPY --chown=myuser:mygroup --chmod=644 files* /somedir/

  Если корневая файловая система контейнера не содержит ни файлов /etc/passwd, ни /etc/group файлов, а в флаге используются имена пользователей или групп --chown , сборка завершится ошибкой COPY. Использование числовых идентификаторов не требует поиска и не зависит от содержимого корневой файловой системы контейнера.

  Примечание:
  Если вы строите с использованием STDIN ( docker build - < somefile), контекст сборки отсутствует, поэтому его COPY нельзя использовать.

  Дополнительно COPY принимает флаг --from=<name>, который можно использовать для установки исходного местоположения на предыдущую стадию сборки (созданную с помощью FROM .. AS <name>), которая будет использоваться вместо контекста сборки, отправленного пользователем. В случае, если этап сборки с указанным имени не может быть найден, вместо него делается попытка использовать образ с таким же именем.

  COPY подчиняется следующим правилам:
 1. Путь <src> должен быть внутри контекста сборки; вы не можете COPY ../something /something, потому что первым шагом docker build является отправка каталога контекста (и подкаталогов) демону докера.
 2. Если <src> это каталог, копируется все содержимое каталога (только его содержимое), включая метаданные файловой системы.
 3. Если <src> это файл любого другого типа, он копируется отдельно вместе с его метаданными. В этом случае, если <dest> заканчивается косой чертой /, он будет считаться каталогом, а содержимое <src> будет записано по адресу <dest>/base(<src>).
 4. Если указано несколько <src> ресурсов, либо напрямую, либо из-за использования подстановочного знака, то это <dest> должен быть каталог, и он должен заканчиваться косой чертой /.
5. Если <dest> не заканчивается косой чертой, он будет считаться обычным файлом, а содержимое <src> будет записано в <dest>.
 6. Если <dest> не существует, он создается вместе со всеми отсутствующими каталогами на его пути.

  Примечание:
  Первая обнаруженная COPY инструкция сделает кэш недействительным для всех последующих инструкций из Dockerfile, если содержимое файла <src> изменилось. Это включает в себя аннулирование кеша для RUN инструкций. Дополнительную информацию см. в Dockerfile руководстве по передовым методам — использование кэша сборки.