if [ ! -f /sbin/ifconfig ] 
then
	echo "setup"
	apt update -y
	apt upgrade -y
	apt install git -y
	apt install wget -y
	apt update -y
	apt upgrade -y
	apt install net-tools
else [ -f /sbin/ifconfig ] 
	echo "root"
fi

