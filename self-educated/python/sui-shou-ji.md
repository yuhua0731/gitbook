---
description: 随手记录的草稿本，鸣谢：chatgpt
---

# ✏️ 随手记

## random

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

## defaultdict

{% code lineNumbers="true" %}
```python
from collections import defaultdict

# Create a defaultdict with defaultdict(int) as the default factory function for nesting
nested_defaultdict = defaultdict(lambda: defaultdict(int))
```
{% endcode %}

## negative base

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

## TLE

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



