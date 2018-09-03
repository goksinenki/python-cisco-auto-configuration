# python-cisco-auto-configuration

Cisco Network Automation - Software Defined Network - System Automation

That's a Cisco switch management program that allow technicians to manage Cisco Switch ports without login directly to switches and without any CLI commands.

You can manage you network switches with a user friendly menu and execute any SSH commands to manage the switches.

In our example:

You can find free switch ports (0 packets), you can change the vlan id or port configuration for allowed switches...etc

By the way, anyone can manage the switches and critical devices without SSH permissions also there is no way to make mistake :)

INSTALLATION (Windows/Linux)

Installation

Just install the required modules/libraries to your python project directory if you do not have them

paramiko

For example:

pip install paramiko

Open ipler.txt and replace ip addresses and hostnames with your network device ipaddresses. 

Open portmanager.py and replace the required information with yours. (ssh username, ssh password, cisco enable password, email addresses, mail server information, vlan ids, port configuration commands...etc)

Then, execute portmanager.py

Do not forget to allow mail relay from your mail server for your script.

Here is a screenshot below.

![alt text](https://github.com/goksinenki/python-cisco-auto-configuration/blob/master/portmanager2.PNG)

Also, you can use that script for all devices/servers/clients that you can connect via SSH. (vendor free)

That's all !
