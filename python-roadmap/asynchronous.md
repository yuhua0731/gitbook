---
description: Asynchronous programming in python
---

# Asynchronous

## Intro

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
