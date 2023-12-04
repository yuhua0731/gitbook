# ScanHome扫码器

## 配置扫码器

连接扫码器后，听到扫码器启动音效，分别对以下配置二维码进行扫码

{% tabs %}
{% tab title="恢复出厂设置" %}
<figure><img src="../.gitbook/assets/image.png" alt="" width="375"><figcaption></figcaption></figure>
{% endtab %}

{% tab title="USB HID-KBW" %}
<figure><img src="../.gitbook/assets/image (2).png" alt="" width="375"><figcaption></figcaption></figure>
{% endtab %}

{% tab title="没有结束符" %}
<figure><img src="../.gitbook/assets/img_v3_025q_f9d4d317-9be6-4221-b2d9-d4168f1a900g.jpg" alt="" width="375"><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

## 下载脚本

{% file src="../.gitbook/assets/main.py" %}

{% file src="../.gitbook/assets/hid_scanner.py" %}

## Mac下运行脚本

1. install hidapi: `brew install hidapi`&#x20;
2. install hidapi module: `python3 -m pip install hidapi`
3. run script: `sudo python3 main.py`
4. 对任意条码进行扫码，脚本输出如下：

```bash
> sudo python3 main.py
Password:
Manufacturer: SM
Product: SM-2D PRODUCT HID KBW
Serial No: APP-000000000
Read the data
len: 13
4902505337611
^CCtrl+C captured, ending read.
```
