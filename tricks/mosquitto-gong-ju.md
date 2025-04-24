# mosquitto工具

## Install

```bash
# use 'mosqui' to start a mqtt broker with port 1883
alias mosqui='/usr/local/sbin/mosquitto -c /usr/local/etc/mosquitto/mosquitto.conf'

mosquitto version 2.0.18

mosquitto is an MQTT v5.0/v3.1.1/v3.1 broker.

Usage: mosquitto [-c config_file] [-d] [-h] [-p port]

 -c : specify the broker config file.
 -d : put the broker into the background after starting.
 -h : display this help.
 -p : start the broker listening on the specified port.
      Not recommended in conjunction with the -c option.
 -v : verbose mode - enable all logging types. This overrides
      any logging options given in the config file.

See https://mosquitto.org/ for more information.

> mosqui
1708232136: mosquitto version 2.0.18 starting
1708232136: Config loaded from /usr/local/etc/mosquitto/mosquitto.conf.
1708232136: Starting in local only mode. Connections will only be possible from clients running on this machine.
1708232136: Create a configuration file which defines a listener to allow remote access.
1708232136: For more details see https://mosquitto.org/documentation/authentication-methods/
1708232136: Opening ipv4 listen socket on port 1883.
1708232136: Opening ipv6 listen socket on port 1883.
1708232136: mosquitto version 2.0.18 running
```

## **Connection Refused 问题**

**修改MQTT代理配置：** 查找MQTT代理的配置文件（如Mosquitto的`mosquitto.conf`），并确认或更改监听地址设置。例如，对于Mosquitto，确保配置文件中有一行如下（或添加这行）：

```yaml
listener 1883 0.0.0.0
```

这行命令让Mosquitto监听所有网络接口上的1883端口。

<figure><img src="../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
当配置文件中没有定义`listener`时，`allow_anonymous`的默认值为`true`，允许匿名连接，但仅允许通过`localhost`进行连接，即从本机连接。

当配置文件中定义了`listener`时，`allow_anonymous`的默认值由`true`变为`false`，不允许匿名连接，连接会由于未授权而断开，为了测试方便，可手动修改为<mark style="color:yellow;">`true`</mark>，允许该`listener`接受匿名连接。
{% endhint %}

检查MQTT代理的配置文件（如`mosquitto.conf`），查看是否有关于允许匿名连接的设置，例如`allow_anonymous`。如果设置为`false`，则需要提供有效的认证信息。

<figure><img src="../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

## 捕捉到终止信号并关闭mqtt客户端

```python
import sys, signal
from mqtt_client import MQTTClient

# 定义一个带自定义参数的函数
def create_signal_handler(mqtt_client: MQTTClient):
    def signal_handler(signum, frame):
        print("")
        print(f"捕获到信号: {signum}")
        # 在这里执行所有实例的deinit操作
        # 比如关闭文件、数据库连接、停止线程等清理工作
        print("执行清理操作...")
        mqtt_client.stop()
        print("退出程序")
        sys.exit(0)  # 退出程序
    return signal_handler

# 创建信号处理器闭包实例
handler = create_signal_handler(mqtt_client)

# 注册信号处理函数
signal.signal(signal.SIGINT, handler)
signal.signal(signal.SIGTERM, handler)
```
