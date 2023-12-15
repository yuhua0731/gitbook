---
description: Asynchronous programming in python
---

# Asynchronous

{% hint style="success" %}
[https://realpython.com/async-io-python/](https://realpython.com/async-io-python/)
{% endhint %}

> **This is a line that provide a great example of native English phrases when writing tech docs**
>
> **"Note**: In this article, I <mark style="color:green;">use the term</mark> **async IO** <mark style="color:green;">to denote</mark> the language-agnostic design of asynchronous IO, while `asyncio` <mark style="color:green;">refers to</mark> the Python package."

## Intro

### asyncio:

* **`async`/`await`**: two new [Python keywords](https://realpython.com/python-keywords/) that are used to define coroutines

### **Parallelism & Concurrency:**

* 并发性

### [Coroutine function](https://docs.python.org/3/reference/compound\_stmts.html#coroutine-function-definition):&#x20;

* Functions defined with `async def` syntax are always coroutine functions
* Execution of Python coroutines can be <mark style="color:yellow;">suspended and resumed at many points</mark> (see [coroutine](https://docs.python.org/3/glossary.html#term-coroutine)).
* [`await`](https://docs.python.org/3/reference/expressions.html#await) expressions, [`async for`](https://docs.python.org/3/reference/compound\_stmts.html#async-for) and [`async with`](https://docs.python.org/3/reference/compound\_stmts.html#async-with) can <mark style="color:yellow;">only be used in the body</mark> of a coroutine function.
* It is a [`SyntaxError`](https://docs.python.org/3/library/exceptions.html#SyntaxError) to use a `yield from` expression inside the body of a coroutine function.

## Installation

```bash
python -m pip install aiohttp beautifulsoup4
```

## Examples

* `asyncio.run()` create an <mark style="color:yellow;">asyncio event loop</mark>
* It is <mark style="color:yellow;">not allowed to run multiple</mark> asyncio event loops in a single thread

```python
import asyncio

async def main():
    await asyncio.sleep(1)
    print('hello')

asyncio.run(main()) # Execute the coroutine and return the result

```

### `async & await`

* when you use `await f()`, it’s required that `f()` be an object that is [awaitable](https://docs.python.org/3/reference/datamodel.html#awaitable-objects).
* an awaitable object is either&#x20;
  1. another coroutine
  2. an object defining an `.__await__()` dunder method that returns an iterator

```python
async def f(x):
    y = await z(x)  # OK - `await` and `return` allowed in coroutines
    return y

async def g(x):
    yield x  # OK - this is an async generator

async def m(x):
    yield from gen(x)  # No - SyntaxError

def m(x):
    y = await z(x)  # Still no - SyntaxError (no `async def` here)
    return y
```

### `asyncio.gather(*coros_or_futures, return_exceptions=False)`

* coroutines are executed <mark style="color:yellow;">independently</mark>
* coroutines returned <mark style="color:yellow;">results</mark> will form a list, with the <mark style="color:yellow;">same order</mark> as they were passed in

```python
import asyncio

async def count(i):
    print("One", i)
    await asyncio.sleep(i)
    print("Two", i)
    return i

async def main():
    print(await asyncio.gather(count(3), count(2), count(1)))

if __name__ == "__main__":
    asyncio.run(main())
    
"""
One 3
One 2
One 1
Two 1
Two 2
Two 3
[3, 2, 1]
"""
```

