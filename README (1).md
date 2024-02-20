# Github ssh keys

## Follow the instruction

{% embed url="https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent" %}
Official Instruction
{% endembed %}

Note: do not ignore the ssh-agent part

<figure><img src=".gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

## Related Issue

{% hint style="info" %}
[https://github.com/orgs/community/discussions/55269](https://github.com/orgs/community/discussions/55269)
{% endhint %}

<figure><img src=".gitbook/assets/image (3).png" alt=""><figcaption><p>This solution works for me!</p></figcaption></figure>

## 🥳最终.ssh/config中存在以下信息

```
Host github.com
  	AddKeysToAgent yes
	Hostname 20.200.245.248
  	Port 443
  	IdentityFile ~/.ssh/id_ed25519
```
