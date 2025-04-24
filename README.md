---
description: 一些适用于zshrc的环境配置内容
---

# 🫖 zshrc

```bash
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion" # This loads nvm bash_completion

export IDF_PATH=~/esp/esp-idf
export MDF_PATH=~/esp/esp-mdf

alias ll='ls -al'
# use 'get_esp' to append the correct path to the idf toolchain
alias get_esp='export PATH=$HOME/esp/xtensa-esp32-elf/bin:$PATH'
# use 'idf' to load esp-idf
alias idf='. ~/esp/esp-idf/export.sh'
# use 'mdf' to load esp-mdf
alias mdf='. ~/esp/esp-mdf/export.sh'
# use 'mosqui' to start a mqtt broker with port 1883
alias mosqui='/usr/local/sbin/mosquitto -c /usr/local/etc/mosquitto/mosquitto.conf'
alias airport="/System/Library/PrivateFrameworks/Apple80211.framework/Versions/A/Resources/airport"
alias webScraper="source ~/virtualenv/webScraper/bin/activate"

export M2_HOME=/Users/huayu/Downloads/apache-maven-3.8.2
export PATH=$PATH:$M2_HOME/bin
export PATH=$PATH:/Users/huayu/hcrobot/gitlab/shuttle-mqtt-test
export PYTHONPATH="/Users/huayu/hcrobot/gitlab/pylib"
export PYTHONPATH=$PYTHONPATH:/Users/huayu/hcrobot/yuhua_test/explore_leet/my_lib

# configure zephyr base
# export ZEPHYR_BASE=/opt/nordic/ncs/v2.3.0/zephyr/

source ~/.zsh/zsh-autosuggestions/zsh-autosuggestions.zsh
source ~/.zsh/fast-syntax-highlighting/fast-syntax-highlighting.plugin.zsh

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh

# autojump startup command
[ -f /usr/local/etc/profile.d/autojump.sh ] && . /usr/local/etc/profile.d/autojump.sh
```

