cat <<EOF | sudo tee /etc/systemd/system/flask-example2.service
[Unit]
Description=flask-example2

[Service]
WorkingDirectory=/opt/flask-example2/
ExecStart=/usr/bin/gunicorn --certfile=cert.pem --keyfile=key.pem --bind 0.0.0.0:443 server:app

[Install]
WantedBy=multi-user.target
EOF
