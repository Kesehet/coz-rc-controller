
sudo apt update -y && sudo apt upgrade -y

sudo apt install git python3 python3-pip

git clone https://github.com/Kesehet/coz-rc-controller.git
cd coz-rc-controller
pip3 install -r requirements.txt 




systemctl restart unattended-upgrades.service


echo "Installing Extra modules for VRF"
sudo apt install linux-modules-extra-$(uname -r) -y

echo "Configuring sysctl"
   sudo modprobe mpls_router
   sudo modprobe mpls_iptunnel
 sudo sysctl -w net.mpls.conf.eth0.input=1
    sudo sysctl -w net.mpls.platform_labels=1000



echo "net.ipv4.ip_forward = 1" | sudo tee -a /etc/sysctl.conf
echo "net.ipv6.conf.all.forwarding = 1" | sudo tee -a /etc/sysctl.conf
echo "net.ipv4.conf.all.accept_redirects = 0" | sudo tee -a /etc/sysctl.conf
echo "net.ipv4.conf.all.send_redirects = 0" | sudo tee -a /etc/sysctl.conf
echo "net.mpls.conf.eth0.input=1" | sudo tee -a /etc/sysctl.conf
echo "net.mpls.platform_labels=1000" | sudo tee -a /etc/sysctl.conf


sudo sysctl -p

sudo apt update



curl -s https://deb.frrouting.org/frr/keys.asc | sudo apt-key add -
FRRVER="frr-stable"
echo deb https://deb.frrouting.org/frr $(lsb_release -s -c) $FRRVER | sudo tee -a /etc/apt/sources.list.d/frr.list
sudo apt install frr -y



echo "Installing Net Tools"
sudo apt install net-tools -y

sudo apt install libreswan -y


sudo apt install nmap -y
sudo apt install traceroute -y

echo "bgpd=yes" | sudo tee -a /etc/frr/daemons

sudo systemctl restart frr

clear

python3 main.py
