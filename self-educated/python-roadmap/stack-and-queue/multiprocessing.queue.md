---
description: IPC - Interprocess Communication
---

# multiprocessing.Queue

## Popular modules

* `multiprocessing [only support FIFO queue]`
  1. `multiprocessing.Queue [after queue.Queue]`
  2. `multiprocessing.SimpleQueue [simplified to .put() .get() & .empty()]`
  3. `multiprocessing.JoinableQueue [add .task_done() & .join()]`
* `concurrent.futures`

## Share resources&#x20;

### between OS processes vs between threads

> Marshalling in python usually refer to serialization&#x20;
>
> python uses the <mark style="color:yellow;">`pickle`</mark> module for data serialization

* processes don't share a common memory region, thus data must be marshalled and unmarshalled during transmission

{% hint style="info" %}
we should consider to switch to multiple processes when:

the performance improvement > the additional data serialization time
{% endhint %}

## Example: Reversing an MD5 hash

```python
import multiprocessing
# check the number of processors of your PC
print(multiprocessing.cpu_count())
```

### Single thread

{% hint style="warning" %}
&#x20;6 letters from 26 lowercase letters gives a total of 308,915,776 combinations, which makes python to compute in several seconds
{% endhint %}

```python
import time
from hashlib import md5
from itertools import product
from string import ascii_lowercase

def reverse_md5(hash_value, alphabet=ascii_lowercase, max_length=6):
    for length in range(1, max_length + 1):
        for combination in product(alphabet, repeat=length):
            text_bytes = "".join(combination).encode("utf-8")
            hashed = md5(text_bytes).hexdigest()
            if hashed == hash_value:
                return text_bytes.decode("utf-8")

if __name__ == "__main__":
    # single thread
    t1 = time.perf_counter()
    text = reverse_md5("a9d1cbf71942327e98b40cf5ef38a960")
    print(f"{text} (found in {time.perf_counter() - t1:.1f}s)") 
    # output: queue (found in 14.7s)
```

### Distribute workload

* break down to several disjoint subsets
* generate a set combinations, and assign each workers some jobs to compute
* create some workers, with <mark style="color:yellow;">`multiprocessing.Process`</mark> as base class

```python
import multiprocessing

class Worker(multiprocessing.Process):
    def __init__(self, queue_in, queue_out, hash_value):
        super().__init__(daemon=True)
        self.queue_in = queue_in
        self.queue_out = queue_out
        self.hash_value = hash_value

    def run(self):
        while True:
            job = self.queue_in.get()
            if job is POISON_PILL:
                self.queue_in.put(POISON_PILL)
                break
            if plaintext := job(self.hash_value):
                self.queue_out.put(plaintext)
                break
```

* for full example's code, check out [https://github.com/yuhua0731/python-roadmap/blob/main/materials-queue/src/multiprocess\_queue.py](https://github.com/yuhua0731/python-roadmap/blob/main/materials-queue/src/multiprocess\_queue.py)

