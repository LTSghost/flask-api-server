FROM python:3.11

RUN mkdir flask-project 

COPY . /flask-project

# ADD . /flask-project

# In general, it's recommended to use COPY for most cases, 
# as it is more straightforward and predictable. 
# Use ADD only when you specifically need its additional functionality, 
# such as handling remote URLs or tar archives.

# RUN echo "MYSQL_USERNAME=root\n\
# MYSQL_PASSWORD=PassW0rd\n\
# MYSQL_DB_ADDRESS=172.18.0.2\n\
# MYSQL_PORT=3306\n\
# MYSQL_DB=quasar_test\n\
# SERVER_PORT=7777" > flask-project/.env

# CMD pip3 install -r requirements.txt

# CMD ["cd flask-project", "pwd"]

# CMD ["source .venv/bin/activate", "python3 run.py"]

# RUN printf '#!/bin/bash\nwhile true\ndo\n   echo \"Press [CTRL+C] to stop..\"\n    sleep 2\ndone' > /loop.sh

# CMD cd flask-project;source .venv/bin/activate;

# CMD ["python3", "/app/run.py"]