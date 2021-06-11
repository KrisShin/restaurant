# !/bin/bash

gunicorn gevent -w 2 -b 0.0.0.0:9096 manage:manage