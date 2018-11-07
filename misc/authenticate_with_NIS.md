# how to setup a NIS server
## Server
    Edit /etc/yp.conf:
    domain internal server ip.of.nis.server

    Edit /etc/ypserv.conf:
    dns: no
    files: 30
    xfr_check_port: yes
    * : * : shadow.byname : port
    * : * : passwd.adjunct.byname : port 

    Edit /etc/sysconfig/network:
    NISDOMAIN="internal"
    Set NIS domain name:

    master# domainname internal
    master# ypdomainname internal
    
    Create file /var/yp/securenets:
    host 127.0.0.1
    255.255.255.0   10.0.0.0
    
    service ypserv start
    service ypbind start

## Client:
    authconfig --enablenis --nisdomain synopsys.com --nisserver l-djy8m12-lnx.internal.synopsys.com --update
    http://bradthemad.org/tech/notes/redhat_nis_setup.php
