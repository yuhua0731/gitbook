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

