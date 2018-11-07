# how to setup a NIS server
    Edit /etc/yp.conf:
    domain internal server ip.of.nis.server

    Edit /etc/ypserv.conf:

    dns: no
    files: 30
    xfr_check_port: yes
    * : * : shadow.byname : port
    * : * : passwd.adjunct.byname : port 
