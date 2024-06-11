# Orangepi

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
