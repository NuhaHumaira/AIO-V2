#!/bin/bash
# REPO
REPO="https://raw.githubusercontent.com/Catzburry/AIO-V2/main/"

#install
cd /root
apt update && apt upgrade
apt install python3 python3-pip git
wget -q ${REPO}bot/xolpanel.zip
unzip xolpanel.zip
rm xolpanel.zip
pip3 install -r xolpanel/requirements.txt
pip3 install pillow

#isi data
rm /root/xolpanel/var.txt
clear
clear
read -e -p "[*] Input your Bot Token : " bottoken
read -e -p "[*] Input Your Id Telegram :" admin
read -e -p "[*] Input Your Subdomain :" domain
echo -e BOT_TOKEN='"'$bottoken'"' >> /root/xolpanel/var.txt
echo -e ADMIN='"'$admin'"' >> /root/xolpanel/var.txt
echo -e DOMAIN='"'$domain'"' >> /root/xolpanel/var.txt
clear
echo "Done"
echo "Your Data Bot"
echo -e "==============================="
echo -e "Bot Token     : $bottoken"
echo -e "Id Telegram   : $admin"
echo -e "Subdomain     : $domain"
echo -e "==============================="
echo "Setting done Please wait 10s"
sleep 5

cat > /etc/systemd/system/xolpanel.service << END
[Unit]
Description=Simple XolPanel - @XolPanel
After=network.target

[Service]
WorkingDirectory=/root
ExecStart=/usr/bin/python3 -m xolpanel
Restart=always

[Install]
WantedBy=multi-user.target
END

systemctl start xolpanel
systemctl enable xolpanel

clear

echo -e "==============================================="
echo -e "Installations complete, type /menu on your bot"
echo -e "==============================================="
read -n 1 -s -r -p "Press any key to Reboot"
rm -rf xolpanel.sh
clear
reboot
