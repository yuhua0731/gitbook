# command line

## `sudo` traps

问题：使用sudo运行python脚本时，import报错

[https://stackoverflow.com/questions/50315645/cannot-run-python-script-using-sudo](https://stackoverflow.com/questions/50315645/cannot-run-python-script-using-sudo)

By default sudo runs commands in different environment. You can ask sudo to preserve environment with `-E` switch.

```python
sudo -E python myScriptName.py
```

