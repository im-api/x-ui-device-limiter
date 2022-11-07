# x-ui-device-limiter
Limit Number of IP's that can connect to a single user of x-ui

Installing dependencies:

Debian\Ubuntu:

```apt update```

```apt install python3 -y && apt install python3-pip -y && pip3 install requests && pip3 install schedule && apt install net-tools -y && apt install screen -y```


CentOS:

```yum install python3 -y && yum install python3-pip -y && pip3 install requests && pip3 install schedule && yum install net-tools -y && yum install screen -y && yum install nano -y```


Run command below at the background:

```python3 limiter.py```
