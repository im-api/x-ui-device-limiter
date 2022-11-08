# x-ui-device-limiter
Limit Number of IP's that can connect to a single user of x-ui

Installing dependencies:

Debian\Ubuntu:

```apt update```

```apt install python3 -y && apt install python3-pip -y && pip3 install requests && pip3 install schedule && apt install net-tools -y && apt install screen -y```


CentOS:

```yum install python3 -y && yum install python3-pip -y && pip3 install requests && pip3 install schedule && yum install net-tools -y && yum install screen -y && yum install nano -y```


Clone Project:

```git clone https://github.com/im-api/x-ui-device-limite```

Go to the project directory:

```cd x-ui-device-limiter```

Edit limiter.py based on what you need:

e.g: you want limit to maximum 5 ip's on each account you have to change _max_allowed_connections = 1 to 5
e.g2: you want script run every 1 houre you have to change _checkCycle = 5 to _checkCycle = 3600


Run command below at the background:

```python3 limiter.py```
