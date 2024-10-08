---
description: from queue import LifoQueue, PriorityQueue, Queue
---

# Thread-Safe Queues

## Installation

Install the [Rich](https://pypi.org/project/rich/) library

This will let you add colors, [emojis](https://en.wikipedia.org/wiki/Emoji), and visual components to your terminal

```bash
(venv) $ python -m pip install rich
```

## Practice

> [https://github.com/yuhua0731/python-roadmap](https://github.com/yuhua0731/python-roadmap)
>
> run `thread_safe_queues.py`

### use fifo, and produce faster than consume

* `python3 thread_safe_queues.py -q fifo -p 2 -c 2 -ps 8 -cs 2`

### <mark style="color:yellow;">maxsize</mark> keyword

* specify maxsize, then new item produced will be blocked if queue is full

<figure><img src="../../../.gitbook/assets/image (13).png" alt=""><figcaption><p>specify non-zero maxsize when initializing a queue</p></figcaption></figure>

## [Asynchronous Queues](https://app.gitbook.com/o/Mn9MdOeo1gYqJ3t2eDyE/s/CQCTmD2dmvBk81v6yd7L/\~/changes/36/python-roadmap/asynchronous) <a href="#using-asynchronous-queues" id="using-asynchronous-queues"></a>

There’s recently been a <mark style="color:yellow;">single-threaded</mark> alternative to synchronized queues, taking advantage of [Python’s asynchronous features](https://realpython.com/python-async-features/).
