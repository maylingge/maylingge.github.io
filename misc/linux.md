# TOP command

*对于内存监控，在top里我们要时刻监控第五行swap交换分区的used，如果这个数值在不断的变化，说明内核在不断进行内存和swap的数据交换，这是真正的内存不够用了。*

*k 终止一个进程。*

*c 切换显示命令名称和完整命令行*

*l 切换显示平均负载和启动时间信息*

http://www.cnblogs.com/peida/archive/2012/12/24/2831353.html 


# Locale (区域设置)
    LANG=en_US.UTF-8
    LC_CTYPE="en_US.UTF-8"
    LC_NUMERIC="en_US.UTF-8"
    LC_TIME="en_US.UTF-8"
    LC_COLLATE="en_US.UTF-8"
    LC_MONETARY="en_US.UTF-8"
    LC_MESSAGES="en_US.UTF-8"
    LC_PAPER="en_US.UTF-8"
    LC_NAME="en_US.UTF-8"
    LC_ADDRESS="en_US.UTF-8"
    LC_TELEPHONE="en_US.UTF-8"
    LC_MEASUREMENT="en_US.UTF-8"
    LC_IDENTIFICATION="en_US.UTF-8"
    LC_ALL=

    locale相关（环境）变量生效的优先顺序：[1]
    LANGUAGE 指定个人对语言环境值的主次偏好，例如zh_CN:en_US:en
    LC_ALL 这不是一个环境变量，是一个可被C语言库函数setlocale设置的宏，其值可覆盖所有其他的locale设定。因此缺省时此值为空
    LC_xxx 可设定locale各方面（category）的值，可以覆盖LANG的值。
    LANG 指定默认使用的locale值
    可以把上述环境变量设在/etc/profile 或 /etc/environment等系统初始文件中。值得注意的是，若LANG或LC_ALL被设定为 "C"，那么LANGUAGE的值将被忽视。 [2]
    除 C 和 POSIX这两个locale名称外，locale的名称并未标准化。Linux平台与Windows系统的locale名称有很大不同。Linux名称的命名规则为：
     language[_territory[.codeset]][@modifier]
