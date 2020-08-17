#!/usr/bin/env bash
# Sets up server file structure automatically
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
touch /data/web_static/releases/test/index.html
echo 'Holberton School' > /data/web_static/releases/test/index.html
ln -s /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data/
