# из unix time  в UTC:

import time

int(time.mktime(time.strptime('2023-12-24 22:19:00', '%Y-%m-%d %H:%M:%S')))
1703445540

float(time.mktime(time.strptime('2023-12-24 22:19:00', '%Y-%m-%d %H:%M:%S')))
1703445540.0

float(time.mktime(time.strptime('2023-12-24 22:19:56', '%Y-%m-%d %H:%M:%S')))
1703445596.0

------------------------------------------------------------
# из unix time в UTC:
import time
 
unix_timestamp = "1284101485"
unix_timestamp = float(unix_timestamp)
time_struct = time.gmtime(unix_timestamp)    # для GMT
time_struct = time.localtime(unix_timestamp) # для local time
 
print(time.strftime("%Y.%m.%d %H:%M:%S", time_struct))