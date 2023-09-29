chmod +x seam
rm -rf /data/data/com.termux/files/usr/bin/seam
rm -rf /data/data/com.termux/files/rms.py
rm -rf /data/data/com.termux/files/hex.py
rm -rf /data/data/com.termux/files/sto.py
rm -rf /data/data/com.termux/files/termux.json
rm -rf /data/data/com.termux/files/usr/etc/bash.bashrc

cp seam -t /data/data/com.termux/files/usr/bin
cp data/rms.py -t /data/data/com.termux/files
cp data/hex.py -t /data/data/com.termux/files
cp data/sto.py -t /data/data/com.termux/files
cp data/termux.json -t /data/data/com.termux/files
cp data/bash.bashrc -t /data/data/com.termux/files/usr/etc

cd /data/data/com.termux/files/home


seam
