# Yield

`yield` 是一个关键字，它用于定义<mark style="color:yellow;">生成器</mark>函数。生成器函数是一种特殊的函数，它可以暂停执行并保存当前的状态，然后在下次调用时从<mark style="color:yellow;">暂停的地方继续</mark>执行，这使得它非常适合处理大量数据或者需要按需生成数据的情况。

在一个函数中使用多个 `yield` 语句时，每次调用 `yield` 会暂停函数的执行，并返回一个值给调用者，同时保存当前的状态。下次调用 `next()` 方法时，函数会从上一次暂停的位置继续执行。

```python
a = [i for i in range(5)]

def get_a(a: list):
    yield a[0]
    for i in a[1:]:
        yield i

# option 1
mask = get_a(a)
print(next(mask), next(mask))
print('-' * 10)
for tt in mask:
    print(tt)
    
# output 1
0 1
----------
2
3
4
    
# option 2
print(get_a(a), get_a(a))
print('-' * 10)
for tt in get_a(a):
    print(tt)
    
# output 2
<generator object get_a at 0x10ef713c0> <generator object get_a at 0x10ef712f0>
----------
0
1
2
3
4
```

<details>

<summary>两种示例使用方式的区别</summary>

从示例代码的执行结果可以看出，每次调用`get_a`方法时，会重新创建并返回一个生成器对象，而不是返回`yield`的内容。

使用A表示一个生成器对象，当我们使用<mark style="color:yellow;">`next(A)`</mark>或<mark style="color:yellow;">`for i in A`</mark>时，我们才能够获取到yield的返回值。

使用时请注意，当我们需要多次并持续性的获取`yield`返回值时，请勿多次创建生成器，否则，可能会导致返回值的顺序不符合预期。而当我们需要重新开始执行生成器内代码时，可以重新调用一次`get_a()`

</details>
