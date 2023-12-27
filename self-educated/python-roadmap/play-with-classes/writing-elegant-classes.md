---
description: python中类的定义及常用方法应用
---

# writing elegant classes

## build-in methods

### `__str__`

`allow your class to be converted to string - str(A) & print(A)`

* `__str__` 用于返回一个用户友好的字符串，通常用于描述对象的特征，是面向<mark style="color:yellow;">用户</mark>的。
* 当你使用 `str()` 函数或者 `print()` 函数来打印一个对象时，`str` 函数会尝试调用该对象的 `__str__` 方法来获取其字符串表示形式。

### `__repr__`

* `__repr__` 用于返回一个开发者友好的字符串，通常用于调试和开发过程中，是面向<mark style="color:yellow;">开发者</mark>的。
* 当你在交互式环境中直接输入一个对象的名称时，会调用该对象的 `__repr__` 方法来获取其字符串表示形式。比如：在终端中进行python3实时调试时

{% hint style="info" %}
如果你只重写了 `__repr__` 方法而没有重写 `__str__` 方法，那么在调用 `print()` 函数时，Python 会默认使用对象的 `__repr__` 方法来获取字符串表示形式。
{% endhint %}

### `__lt__(self, other)`

`less than, implement this to allow class A being able to be compared with each other`

{% code lineNumbers="true" %}
```python
import heapq

class A:
    def __init__(self, value):
        self.value = value

    # 定义 __lt__ 方法，用于在类的实例之间进行比较
    def __lt__(self, other):
        return self.value < other.value

# 创建包含类 A 实例的列表
heap = [A(5), A(3), A(7), A(1)]

# 使用 heapq.heapify 对列表进行堆化
heapq.heapify(heap)

# 现在 heap 中的元素会按照 __lt__ 方法定义的规则排序

# 通过弹出堆顶元素可以获取到最小值
min_element = heapq.heappop(heap)
print(min_element.value)  # 输出 1

"""
if __lt__ is not implemented, the following error will be raised

TypeError: '<' not supported between instances of 'A' and 'A'
"""
```
{% endcode %}

### `__iter__(self) & __next__(self)`

`make your class instances usable in a` [`for loop`](https://realpython.com/python-for-loop/)

```python
# 第一种实现方式，仅实现__iter__()方法，通过yield关键字实现每次调用获取一个元素
def __iter__(self):
    for index in range(self.size):
        yield self.elements[index]

# 第二种实现方式，实现__iter__()与__next__()方法，iter方法返回类的实例
# 而next方法被用来获取下一个元素
def __iter__(self):
    self.index = 0
    return self

def __next__(self):
    if self.index < len(self.elements):
        result = self.elements[self.index]
        self.index += 1
        return result
    else:
        raise StopIteration
```

{% hint style="success" %}
上面给出的示例实现了一个完整的迭代器协议，包括`__iter__`和`__next__`方法。`__iter__`方法返回一个迭代器对象，而`__next__`方法用于在每次迭代中返回下一个元素。这种方式更加直接和传统。

以下是两种方式之间的主要区别：

1. **实现方式**:
   * 第一个代码块实现了一个生成器函数作为迭代器，使用`yield`语句生成每个元素。这种方式相对更简洁。
   * 第二个代码块实现了一个类，其中`__iter__`方法返回了一个迭代器对象，而`__next__`方法定义了迭代行为。
2. **返回类型**:
   * 第一个代码块返回一个生成器对象，而不是一个类实例。
   * 第二个代码块返回一个自定义的类实例，该实例遵循了迭代器协议。
3. **内部实现**:
   * 第一个代码块使用了一个循环和`yield`来实现迭代，它的实现方式更为灵活。
   * 第二个代码块则采用了更传统的类实现，其中`__next__`方法被显式地调用来获取下一个元素。
4. **使用方式**:
   * 对于用户来说，使用方式是不同的。在第一个代码块中，你可以直接使用`for item in my_custom_list`来迭代，因为生成器本身就是一个可迭代对象。
   * 在第二个代码块中，你需要先创建一个类的实例，然后才能使用`for item in my_custom_list`。
{% endhint %}

### `__len__()`

`make your class compatible with the len() function`

### `__call__()`

By implementing the special method `.__call__()` in a job, you [make objects of your class callable](https://realpython.com/python-callable-instances/).

## built-in fun modules

### count

can be used to continuously get the next count number

```python
from itertools import count

class A:
    def __init__(self):
        self._counter = count(start = 3, step = 2) # default start = 0, step = 1

    def get_count(self):
        return next(self._counter)

a = A()
print(a.get_count()) # 3
print(a.get_count()) # 5
```

## dataclasses

### `@dataclass(order=True)`

the additional <mark style="color:yellow;">`order`</mark> flag, which makes the elements <mark style="color:yellow;">**comparable**</mark>

```python
from dataclasses import dataclass

@dataclass(order=True)
class Element:
    priority: float
    count: int
    value: Any
```

### `@dataclass(frozen=True)`

the additional <mark style="color:yellow;">`frozen`</mark> flag, which make sure that the objects can not be modified

## argparse

```python
def main(args):
    pass

def parse_args():
    parser = argparse.ArgumentParser(description = 'xx arguments')
    parser.add_argument("-d", "--max-depth", type=int, default=2)
    parser.add_argument("-w", "--num-workers", type=int, default=3)
    return parser.parse_args()

if __name__ == "__main__":
    main(parse_args())
```
