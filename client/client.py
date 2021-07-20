import sys
sys.path.append('util')
from multimaster import Multimaster
import os
import socket

class Client:
    def __init__(self, host_ip, interface):
        self.first_setup(host_ip, interface)
        self.setup()
        
    def first_setup(self, host_ip, interface):
        try:
            os.system("export ROS_MASTER_URI=http://" + str(host_ip) + ":11311")
            ip = os.popen('ip addr show ' + interface).read().split("inet ")[1].split("/")[0]

            hosts = open("/etc/hosts", "a")
            hosts.write("\n### AUTOMATED NETWORK CONFIG ###\n")
            hosts.write(str(host_ip) + "\thost\n")
            hosts.write(str(ip) + "\t" + str(socket.gethostname()))

            os.system("export ROS_HOSTNAME=" + str(ip))
            os.system("sudo sh -c 'echo net.ipv4.icmp_echo_ignore_broadcasts=0 >> /etc/sysctl.conf'")
            os.system("sudo service procps restart")

        except IOError:
            print("ERROR, are you running this as root? (sudo client/client.py)")
            sys.exit()
            
    def setup(self):
        multimaster = Multimaster()
        multimaster.setup()
        
# for debugging
client = Client(host_ip="192.168.0.57", interface="wlp59s0")
