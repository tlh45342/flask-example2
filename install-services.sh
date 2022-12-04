cat <<EOF | sudo tee /etc/systemd/system/flask-example2.service
[Unit]
Description=flask-example2

[Service]
WorkingDirectory=/opt/flask-example2/
ExecStart=/usr/local/bin/gunicorn -b 0.0.0.0:443 -w 4 server:app

[Install]
WantedBy=multi-user.t
