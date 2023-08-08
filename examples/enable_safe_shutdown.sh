#!/bin/bash

sudo mv safe_shutdown.py /usr/local/bin/pipower_safe_shutdown
sudo chmod +x /usr/local/bin/pipower_safe_shutdown
sudo mv pipower_safe_shutdown.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable pipower_safe_shutdown