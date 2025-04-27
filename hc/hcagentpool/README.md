---
description: deployed on s003
---

# 🤖 HCAgentPool

{% hint style="success" %}
在Linux系统中搭建代理服务

[https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/v2-linux-agent?view=azure-devops](https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/v2-linux-agent?view=azure-devops)
{% endhint %}

## 获取PAT

{% tabs %}
{% tab title="进入PAT页面" %}
<figure><img src="../../.gitbook/assets/image (18).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="创建PAT" %}
<figure><img src="../../.gitbook/assets/image (19).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="保存PAT（必需）" %}
<figure><img src="../../.gitbook/assets/image (20).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

## 创建及部署Agent

{% tabs %}
{% tab title="进入AgentPool页面" %}
1

<figure><img src="../../.gitbook/assets/image (24).png" alt=""><figcaption></figcaption></figure>

2

<figure><img src="../../.gitbook/assets/image (25).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="新建AgentPool" %}
<figure><img src="../../.gitbook/assets/image (26).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="新建Agent" %}
<figure><img src="../../.gitbook/assets/image (28).png" alt=""><figcaption><p>选择对应的系统，按照配置教程进行配置，Agent列表中会自动更新显示</p></figcaption></figure>
{% endtab %}

{% tab title="Agent运行中" %}
<figure><img src="../../.gitbook/assets/image (29).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

代理服务自启动：

[https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/linux-agent?view=azure-devops#run-as-a-systemd-service](https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/linux-agent?view=azure-devops#run-as-a-systemd-service)

s003部署信息：

```sh
# server
ssh hc@10.0.1.248
Auda2018

# path
/home/hc/devopsagent

# manage service
sudo ./svc.sh start
sudo ./svc.sh status
sudo ./svc.sh stop
```



```sh
export AGENT_TOOLSDIRECTORY="/opt/hostedtoolcache"
# expired
export DEVOPS_ACCESS_TOKEN="6qo2sbx5fl2q7ydd33dsjqbktngsr2sdhipenhnrhnqbgwzniaqa"
# active
export DEVOPS_ACCESS_TOKEN="B1XYmUCWUJYOlsAiLCHNNUOiNzJ3G0CJy1ddIx380NZqyBFWLWC3JQQJ99BCACAAAAAP6MqkAAASAZDOE6nd" 
```

## 部署Pipeline

{% tabs %}
{% tab title="进入Pipelines页面" %}
<figure><img src="../../.gitbook/assets/image (30).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="新建Pipeline" %}
1

<figure><img src="../../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>

2

<figure><img src="../../.gitbook/assets/image (32).png" alt=""><figcaption></figcaption></figure>

3

<figure><img src="../../.gitbook/assets/image (33).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="更新Pipeline" %}
Pipeline依赖工程目录下默认名称为`azure-pipelines.yml`的文件

当需要更新Pipeline时，可通过常规git提交的方式，也可以通过网页界面进行

<figure><img src="../../.gitbook/assets/image (34).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

