import os
os.system('cd /data/data/com.termux/files/usr/etc && rm -rif bash.bashrc') 
os.system('cp bash.bashrc /data/data/com.termux/files/usr/etc')
os.system('cp .__net-tools__.sh /data/data/com.termux/files/home/kali-fs/root')
os.system('cd /data/data/com.termux/files/home/kali-fs/root && rm -rif .bashrc')      
os.system('cp .bashrc /data/data/com.termux/files/home/kali-fs/root')
os.system('cd /data/data/com.termux/files/home/ && rm -rif start-kali.sh')
os.system('cp start-kali.sh /data/data/com.termux/files/home/ && chmod +x start-kali.sh')