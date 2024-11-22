# pi

## Config wireless option

{% embed url="https://sbc-community.org/docs/general_guides/connect_to_wifi/" %}

### List wireless network

```sh
sudo nmcli device wifi list

*  SSID               MODE     CHAN     RATE          SIGNAL      BARS      SECURITY
*  Orange-Pi-wifi     Infra     11       54 Mbit/s      100         ▂▄▆█     --
   A13-Wifi           Infra      6       54 Mbit/s       30          ▂___    WPA1 WPA2
   2WIRE533           Infra     10       54 Mbit/s       44          ▂▄__    WPA1 WPA2
```

### Connect to network

```sh
# connect to a public network
sudo nmcli device wifi connect 'WiFINetworkName' ifname wlan0

# connect to a secure network
sudo nmcli device wifi connect 'WiFiNetworkName' password 'WifiPass' ifname wlan0

# verify the connection
ip -br address show dev wlan0
```

## Reset user password

* 关机，拔出SD卡，插入其他电脑
* 打开SD卡目录，编辑`cmdline.txt`文本文件，在末尾加上`init=/bin/sh`，保存
* 将SD卡插回pi，连接屏幕、键盘，开机，等待光标出现
* 输入
  * `mount -o remount rm /`
  * `passwd pi`
* 提示输入新密码，重复输入两遍，显示密码更新成功
* 输入
  * `sync`
  * `exec /sbin/init`
* pi同步并启动



`mac: B8:27:EB:6B:32:10`&#x20;

`static ip: 10.0.66.77`

`username & password: pi`

![](<../.gitbook/assets/image (35).png>)



