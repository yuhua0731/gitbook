---
description: 随手记录的草稿本，鸣谢：chatgpt
---

# ✏️ 随手记

## 将数字转换成指定位数的binary形式

```python
def helper(x, n):
    return format(x, f'0{n}b')
```

## random模块常用方法

<pre class="language-python" data-line-numbers><code class="lang-python">import random

<strong># Generate a random float between 0.0 and 1.0
</strong>random_float = random.random()

# Generate a random float between a and b
random_float = random.uniform(a, b)

# Generate a random integer between low and high (inclusive)
random_integer = random.randint(low, high)

# Generate a random element based on these probabilities
random_element = random.choices(elements, probabilities)[0]
</code></pre>

## defaultdict嵌套用法

{% code lineNumbers="true" %}
```python
from collections import defaultdict

# Create a defaultdict with defaultdict(int) as the default factory function for nesting
nested_defaultdict = defaultdict(lambda: defaultdict(int))
```
{% endcode %}

## 以负数为基数的进制转换：negative base

```python
def baseNeg2(self, n: int) -> str:
    def divmod_non_negative(a, b):
        quotient, remainder = divmod(a, b)
        if remainder < 0:
            quotient += 1
            remainder -= b
        return quotient, remainder
    
    if n == 0: return '0'
    ret = ''
    while n != 0:
        a, b = divmod_non_negative(n, -2)
        ret += str(b)
        n = a
    return ret[::-1]
```

## 列表多次拷贝导致TLE

```python
# the following list action will get TLE
ret = []
for i in arr:
    ret = [i] + ret
# this will copy the whole list
# generate a new list and point the previous variable to the new list
    
# while, the general append action will beat 100% time
ret = []
for i in arr:
    ret.append(i)
ret = ret[::-1]
```

## 变量rewind处理：Calculate diff in rewind value range

### 计算目标-当前，带方向

如果电机的坐标范围是 `0 ~ 4096`（记为 `range`），则可以使用以下公式：

<figure><img src="../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

#### 公式说明

1. **计算初始差值**：`target - current` 表示目标位置和当前位置的直接差值。
2. **偏移调整**：加上 `range / 2` 来确保结果始终在 `[-range/2, range/2)` 范围内。
3. **取模范围**：使用 `% range` 保证差值在一个周期范围内。
4. **平移回去**：减去 `range / 2`，以获得最小绕行距离，结果可以为正或负。

这个公式可以计算出绕行距离而无需判断逻辑。

### 不关心差值方向，只关心差距

<figure><img src="../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

```cpp
#include <cmath>

int calculatePositionDifference(int current, int target, int range = 4096) {
    // 使用统一公式计算差值
    int difference = ((target - current + range / 2) % range) - range / 2;
    return difference;
}

int calculateAbsoluteDistance(int current, int target, int range = 4096) {
    // 计算直接差距和绕行差距，并取最小值
    int direct_distance = std::abs(target - current);
    int wraparound_distance = range - direct_distance;
    return std::min(direct_distance, wraparound_distance);
}
```

## github PAT

[https://stackoverflow.com/questions/68775869/message-support-for-password-authentication-was-removed](https://stackoverflow.com/questions/68775869/message-support-for-password-authentication-was-removed)

```
2024-11-14: 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
```

From 2021-08-13, GitHub is no longer accepting account passwords when authenticating Git operations. You need to add a **PAT (Personal Access Token)** instead, and you can follow the below method to add a PAT on your system.

> ### Create Personal Access Token on GitHub
>
> From your GitHub account, go to **Settings** → **Developer Settings** → **Personal Access Token** → **Tokens (classic)** → **Generate New Token** (Give your password) → **Fillup the form** → click **Generate token** → **Copy the generated Token**, it will be something like `ghp_sFhFsSHhTzMDreGRLjmks4Tzuzgthdvfsrta`

> ### For Windows OS [⤴](https://support.microsoft.com/en-us/windows/accessing-credential-manager-1b5c916a-6a16-889f-8581-fc16e8165ac0)
>
> Go to **Credential Manager** from **Control Panel** → **Windows Credentials** → find `git:https://github.com` → **Edit** → On Password replace with with your **GitHub Personal Access Token** → You are Done
>
> ###
>
> If you don’t find `git:https://github.com` → Click on **Add a generic credential** → Internet address will be `git:https://github.com` and you need to type in your username and password will be your **GitHub Personal Access Token** → Click Ok and you are done

***

> ### For macOS [⤴](https://docs.github.com/en/get-started/getting-started-with-git/updating-credentials-from-the-macos-keychain)
>
> Click on the Spotlight icon (magnifying glass) on the right side of the menu bar. Type **Keychain access** then press the Enter key to launch the app → In Keychain Access, search for `github.com` → Find the **internet password** entry for `github.com` → Edit or delete the entry accordingly → You are done

## Zphyer SDK

{% embed url="https://docs.zephyrproject.org/latest/develop/toolchains/zephyr_sdk.html" %}

you can also use nRF connect to install the bundle.&#x20;

If it is installed by nRF connect, start terminal by nRF and run the command.

```sh
> python3 json_to_bin.py
Output written to: ./hardware_config/hardware_2_1_x.bin
Successfully created hardware_2_1_x.hex
Successfully delete ./hardware_config/hardware_2_1_x.bin
Output written to: ./hardware_config/hardware_2_0_x.bin
Successfully created hardware_2_0_x.hex
Successfully delete ./hardware_config/hardware_2_0_x.bin
```

