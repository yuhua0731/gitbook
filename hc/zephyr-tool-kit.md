# 🦩 zephyr-tool-kit

{% file src="../.gitbook/assets/zephyr_toolkit-0.3.5.tar.gz" %}
安装包
{% endfile %}

## 安装工具

1. 打开任意`ncs`终端
2. 运行`pip install`安装

```bash
python3 -m pip install zephyr_toolkit-0.3.5.tar.gz
```

## 运行

> 若运行时提示缺少部分python模块，自行安装相应的模块即可

```bash
> ztk -h
usage: ztk [-h] {build,clean,flash,settings,cp,ls,mkdir,mklfs,slcan,lss} ...

Zephyr Tool Kit

options:
  -h, --help            show this help message and exit

extension commands for zephyr:
  {build,clean,flash,settings,cp,ls,mkdir,mklfs,slcan,lss}
    build               build zephyr application
    clean               clean zephyr application
    flash               flash zephyr application
    settings            convert json file to settings file
    cp                  copy file from host to littlefs image
    ls                  list files and directories under the littlefs image
    mkdir               create directory in littlefs image
    mklfs               create littlefs image
    slcan               slcan device tools
    lss                 canopen layer setting service
```

