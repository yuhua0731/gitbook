---
description: 虚拟环境被创建后，可在任意路径进行激活并使用
---

# 🐾 Virtual environment

## Python virtualenv

1. cd to virtualenv directory: `~/virtualenv`
2. `python3.x -m venv "venv-name"` to create new env
3. `source <your virtual env folder>/<your virtual env name>/bin/activate` to active env
4. you can see your virtual env name in your terminal line, like this:
5. `deactivate` to exit current virtual environment

<pre class="language-sh"><code class="lang-sh"> # it is recommanded that you put your virtual environment in your working directory
 > cd ~/virtualenv
 
 # commands to create and activate/deactivate a venv
 > python3.x -m venv "venv-name"
 > source "venv_name"/bin/activate
 ~/virtualenv >                  py mypython 11:22:39                                                                                                  
 > deactivate
 ​
 > pip list # list all packages installed
 <a data-footnote-ref href="#user-content-fn-1">> find . -name "*activate" -type f</a> # bare command list to find all virtual environment in a path
 <a data-footnote-ref href="#user-content-fn-2">>  pipenv --venv # list virtual environment</a>
 > sudo rm -rf "venv_name" # delete a virtual environment
</code></pre>

{% hint style="success" %}
如果出现python版本无法匹配的情况，请更新virtualenv以获取当前使用的python版本\
`pip install --upgrade virtualenv`
{% endhint %}

## Execute a script anywhere in shell

[add `export PATH=$PATH:</path/to/file>` to your `~/.zshrc` file.](#user-content-fn-3)[^3]

## Export python environment to another computer

```sh
 pip freeze > requirements.txt # generate a file which specify all packages install in current environment
 pip install -r requirements.txt # install packages in this file
```

\


[^1]: [https://bobbyhadz.com/blog/list-all-virtual-environments-python](https://bobbyhadz.com/blog/list-all-virtual-environments-python)

[^2]: this line does not work

[^3]: Does not work
