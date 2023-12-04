---
description: 虚拟环境被创建后，可在任意路径进行激活并使用
---

# 🐾 Virtual environment

## Python virtualenv

1. cd to virtualenv directory: `~/virtualenv`
2. `virtualenv <your virtual env name>` to create new env
3. `source <your virtual env folder>/<your virtual env name>/bin/activate` to active env
4. you can see your virtual env name in your terminal line, like this:
5. `deactivate` to exit current virtual environment

```sh
 > cd ~/virtualenv
 > virtualenv mypython
 > source mypython/bin/activate
 ~/virtualenv >                  py mypython 11:22:39                                                                                                  
 > deactivate
 ​
 > pip list # list all packages installed
 > pipenv --venv # list virtual environment
 > python3 -m venv .venv # create new virtual environment for current workspace (macOS.vscode)
```

{% hint style="success" %}
如果出现python版本无法匹配的情况，请更新virtualenv以获取当前使用的python版本\
`pip install --upgrade virtualenv`
{% endhint %}

## Execute a script anywhere in shell

add `export PATH=$PATH:</path/to/file>` to your `~/.zshrc` file.

Does not work

## Export python environment to another computer

```sh
 pip freeze > requirements.txt # generate a file which specify all packages install in current environment
 pip install -r requirements.txt # install packages in this file
```

\
