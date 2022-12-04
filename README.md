# INTRODUCTION

[![Software License](https://img.shields.io/badge/license-Apache%202-blue)](LICENSE)

flask-example2 is a simple example flask app.  It is a simple Hello World! app.
This example is designed to implement SSL, flask_login, and sqlite.
This is not designed to be pretty, or clever. This is simply designed to work.

Work will have been done to test this on Windows 10, Ubuntu 20.04.3 LTS, Apple Mac OS x.

- learning Flask.
- kicking off your a new project.

## INSTALLATION

The small section will discuss how just to simply run the app.  

```bash
git clone https://github.com/tlh45342/flask-example2.git
```

To make sure you have all the python modules installed.

```bash
pip install -r requirements.txt
```
## SIDEBAR: Notes for creating a service for Linux based distributions

I am putting my notes here now - because I will use them.  Consider these notes used to implement the Flask APP as a service.

To create a service entry cd /etc/systemd/system
Create a file that looks something like is found in the following block.
As much as I hate assumptions - you will need to edit this to your tastes and for your environment.

```bash
cat <<EOF | sudo tee /etc/systemd/system/flask-example2.service
[Unit]
Description=flask-example2

[Service]
WorkingDirectory=/opt/flask-example2/
ExecStart=/usr/local/bin/gunicorn -b 0.0.0.0:443 -w 4 server:app

[Install]
WantedBy=multi-user.target
EOF
```

The key commands for reference are: 

```bash
sudo systemctl daemon-reload
sudo systemctl start flask1.service
sudo systemctl restart flask1.service
sudo systemctl stop flask1.service
```

## STRUCTURE

    ├── cert.pem                    A fairly generic cert.   
    ├── Dockerfile                  Dockerfile to creaate as a container   
    ├── key.pem                     The key for the above generic cert. 
    ├── LICENSE                     Copy of the Apache 2.0 license
    ├── requirements.txt            module requirements
    ├── install-service.sh          Shell script to install service script   
    └── server.py                   Wsgi app
 
## LICENSE

flask-example2 is licensed under the Apache License, Version 2.0. See LICENSE for the full license text.

## ACKNOWLEDGEMENTS

Many thanks to Python, Flask and other good stacks.
Please note that this does include http://getskeleton.com/ skeleton.css and normal.css (credit to them)

**URLS:**  
  https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins  
  https://medium.com/analytics-vidhya/how-to-use-flask-login-with-sqlite3-9891b3248324  
>At the last review there were errors in the above medium document (reviewed: 9/4/2021)  
     however I was able to bridge the gap and fill in holes in my knowledge with this.
