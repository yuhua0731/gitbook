# 老版CICD验证方式

我们在`docker container`中编译固件时，需要使用`west update`对依赖的模块进行拉取

为了访问`azure devops`平台上的模块仓库，需要使用`access key`进行验证

使用`/bin/replace_url.sh`脚本，对`west.yml`文件中的`url`进行修改，使其在拉取时包含`access key`

脚本内容如下：

```
#!/bin/bash

# 检查是否提供了文件路径
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <file_path>"
    exit 1
fi

# 检查文件是否存在
if [ ! -f "$1" ]; then
    echo "File not found: $1"
    exit 2
fi

# 执行替换操作
sed -i 's|https://SimplAutomation@dev.azure.com/SimplAutomation/Zephyr/_git|https://oauth2:B1XYmUCWUJYOlsAiLCHNNUOiNzJ3G0CJy1ddIx380NZqyBFWLWC3JQQJ99BCACAAAAAP6MqkAAASAZDOE6nd@dev.azure.com/SimplAutomation/Zephyr/_git|g' "$1"
sed -i 's|http://npd-git.hcrobots.com/embedded|http://yu.hua:Auda2018@npd-git.hcrobots.com/embedded|g' "$1"

echo "URL replacement completed successfully."
```
