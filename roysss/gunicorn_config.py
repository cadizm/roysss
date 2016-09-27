
# http://docs.gunicorn.org/en/latest/settings.html

chdir = '/opt/roysss/roysss'

bind = '127.0.0.1:8002'
proc_name = 'roysss.wsgi'
pidfile = '/opt/roysss/var/run/roysss.pid'

import multiprocessing
workers = multiprocessing.cpu_count() * 2 + 1

reload = True
daemon = False  # use systemd
capture_output = True

user = 'www-data'
group = 'www-data'

accesslog = '/opt/roysss/var/log/access.log'
errorlog = '/opt/roysss/var/log/error.log'
