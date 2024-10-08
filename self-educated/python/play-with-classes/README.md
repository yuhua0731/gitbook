---
coverY: -109
layout:
  cover:
    visible: true
    size: full
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# Play with classes

## Mixin class

{% hint style="info" %}
To reuse code across unrelated classes, you can identify their least common denominator and then extract that code into a [mixin class](https://realpython.com/inheritance-composition-python/#mixing-features-with-mixin-classes). A mixin class is like a spice. It can’t stand on its own, so <mark style="color:yellow;">you wouldn’t typically instantiate it</mark>, but it can add that extra flavor once you mix it into another class.
{% endhint %}

One of the uses of <mark style="color:yellow;">multiple inheritance</mark> in Python is to extend a class features through [mixins](https://en.wikipedia.org/wiki/Mixin). A <mark style="color:yellow;">**mixin**</mark> is a class that provides methods to other classes but are <mark style="color:yellow;">not</mark> considered <mark style="color:yellow;">a base class</mark>. They are <mark style="color:yellow;">similar to composition</mark> but they create a stronger relationship.

Mixins are great for <mark style="color:yellow;">encapsulating</mark> <mark style="color:yellow;"></mark><mark style="color:yellow;">**behavior**</mark> rather than state, much like [default methods](https://docs.oracle.com/javase/tutorial/java/IandI/defaultmethods.html) in [Java](https://realpython.com/java-vs-python/) interfaces.

> **Mixin类**:
>
> * Mixin类是一个具有可重用方法和属性的类，可以通过<mark style="color:yellow;">多继承</mark>的方式来将其混合（mix）到其他类中，以提供额外的功能。
> * Mixin类通常不会被单独实例化，而是通过被混合到其他类中来共享其功能。
> * Mixin类通常用于在多个类之间共享通用行为，从而避免代码重复。
> * 如果两个或多个Mixin类包含相同的方法，Python 将会选择第一个被继承的类中的方法。后继承的Mixin类中的同名方法将会被前面的Mixin类中的同名方法所遮蔽。也就是说，后者将会覆盖前者。
> * Mixin类中使用到的属性和方法，需要在实例类中进行初始化及实现。如果运行期间调用了未初始化的属性，将会抛出`AttributeError`，但如果运行期间不会进行调用，则不会出现问题。

## Abstract class

> **抽象类**
>
> * 抽象类是一个包含抽象方法（<mark style="color:yellow;">只有方法签名</mark>，没有具体实现）的类，它<mark style="color:yellow;">不能被实例化</mark>。
> * 抽象类的目的是为了提供一个接口，让子类实现自己的具体方法。
> * 在Python中，抽象类通常使用 `abc` 模块来定义，使用 `@abstractmethod` 装饰器来标记抽象方法。

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass
```

## Interface
