# Stack & Queue

## Basic definitions:

Stack - LIFO - a stack can be implemented using an array or a linked list

Queue - FIFO - a queue can be implemented using an array

## **Crucial Terms**

Stacks and queues both have an add operation (`push`/`enqueue`) and a remove operation (`pop/dequeue`).

* **push:** (stack) The generic term for adding an object to the "top" of the stack.
* **pop:** (stack) The generic term for removing the object from the "top" of the stack.
* **enqueue:** (queue) The generic term for adding an object to the "back" of the queue.
* **dequeue:** (queue) The generic term for removing an object from the "front" of the queue.
* **Front:** Get the front item from queue – Time Complexity : O(1)
* **Rear:** Get the last item from queue – Time Complexity : O(1)

## General functions:

### Stack

<table data-full-width="true"><thead><tr><th width="158">Operation</th><th width="602">Description</th><th>Time complexity</th></tr></thead><tbody><tr><td><code>push(item)</code></td><td>Pushes <code>item</code> on the "top" of the stack</td><td><code>O(1)</code></td></tr><tr><td><code>pop()</code></td><td>Removes the most recently added item from the stack. (i.e. the item on "top")</td><td><code>O(1)</code></td></tr><tr><td><code>peak()</code></td><td>Accesses the most recently added item in the stack, without removing it</td><td><code>O(1)</code></td></tr><tr><td><code>isEmpty()</code></td><td>Returns <code>True</code> if there are no items on the stack, <code>False</code>otherwise</td><td><code>O(1)</code></td></tr></tbody></table>

### Queue

<table data-full-width="true"><thead><tr><th width="181">Operation</th><th width="529">Description</th><th>Time complexity</th></tr></thead><tbody><tr><td><code>enqueue(item)</code></td><td>Puts <code>item</code> at the end of the queue</td><td><code>O(1)</code></td></tr><tr><td><code>dequeue()</code></td><td>Removes the item at the front of the queue</td><td><code>O(1)</code></td></tr><tr><td><code>peak()</code></td><td>Accesses the item at the front of the queue, without removing it</td><td><code>O(1)</code></td></tr><tr><td><code>isEmpty()</code></td><td>Returns <code>True</code> if there are no items in the queue, <code>False</code>otherwise</td><td><code>O(1)</code></td></tr></tbody></table>

> in Python, there is no specific stack or queue data structure, simply we will use a list to perform both. The time complexity of those function listed above might be <mark style="color:yellow;">slightly worse</mark> than it is defined.

## Samples

Stack & Queue in Python can be implemented using the following ways:&#x20;

* <mark style="color:blue;">`list`</mark>` ``-`` `<mark style="color:blue;">`minimum memory`</mark>` ``needed, but will have`` `<mark style="color:blue;">`reallocate`</mark>` ``issue`
* <mark style="color:blue;">`collections.deque`</mark>` ``- doubly linked list, best choice for non-threaded`
* <mark style="color:blue;">`queue.LifoQueue & queue.Queue`</mark>` ``- fully`` `<mark style="color:blue;">`thread-safe`</mark>

### `list & collections.deque`

[<mark style="color:yellow;">`collections.deque`</mark>](#user-content-fn-1)[^1] <mark style="color:yellow;">is preferred over the list</mark> in the cases where we need quicker append and pop operations from both the ends of the container, as deque provides an <mark style="color:green;">`O(1)`</mark> time complexity for append and pop operations as compared to list which provides <mark style="color:green;">`O(n)`</mark> time complexity.

> The <mark style="color:yellow;">contiguous memory layout</mark> is the reason that `list` might need to take more time to `.append()` some objects than others. If the block of contiguous memory is full, then it will need to <mark style="color:yellow;">get another block</mark>, which can take much longer than a normal `.append()`
>
> `deque`, on the other hand, is built upon a doubly linked list. In a [linked list structure](https://realpython.com/linked-lists-python/), each entry is stored in its own memory block and has a reference to the next entry in the list.

```python
# implement using list
stack = []

stack.append(1)
stack.append(2) # 1, 2

stack.pop() # 2
stack.pop() # 1
```

{% hint style="warning" %}
Note: python's built-in `list` data structure is <mark style="color:yellow;">not a good</mark> implementation for Queue. Since inserting or deleting elements at the beginning requires <mark style="color:yellow;">shifting</mark> all of the other elements by one, which is O(n) time.
{% endhint %}

<pre class="language-python"><code class="lang-python"><strong># implement using deque
</strong><strong>from collections import deque
</strong><strong>
</strong><strong>stack = deque()
</strong><strong>stack.append(1)
</strong><strong>stack.append(2) # 1, 2
</strong><strong>
</strong><strong>stack.pop() # 2
</strong><strong>stack.pop() # 1
</strong><strong>
</strong><strong>queue = deque()
</strong><strong>queue.append(1)
</strong><strong>queue.append(2) # 1, 2
</strong><strong>
</strong><strong>queue.popleft() # 1, O(1) time
</strong><strong>queue.popleft() # 2
</strong></code></pre>

{% hint style="info" %}
`deque` is more <mark style="color:yellow;">flexible</mark>, and can <mark style="color:yellow;">change the direction</mark> dynamically during the runtime

Most deques support two additional operations called <mark style="color:yellow;">rotate left/right</mark>
{% endhint %}

### `queue module`

> `from queue import Queue, LifoQueue`

`Queue` has a <mark style="color:yellow;">maxsize</mark> property, which is the most difference from `collections.deque`

`Queue` module also has a LIFO Queue, which is basically a Stack.

There are various functions available in this module:&#x20;

* **maxsize** – Number of items allowed in the queue.
* **empty()** – Return True if the queue is empty, False otherwise.
* **full()** – Return True if there are _maxsize_ items in the queue. If the queue was initialized with maxsize=0 (the default), then full() never returns True.
* **get()** – Remove and return an item from the queue. If the queue is empty, wait until an item is available.
* <mark style="color:blue;">**get\_nowait()**</mark> – Return an item if one is immediately available, else raise QueueEmpty.
* **put(item)** – Put an item into the queue. If the queue is full, wait until a free slot is available before adding the item.
* <mark style="color:blue;">**put\_nowait(item)**</mark> – Put an item into the queue without blocking. If no free slot is immediately available, raise QueueFull.
* **qsize()** – Return the number of items in the queue.

```python
# implement using Queue
from queue import Queue
from queue import LifoQueue # stack

stack = LifoQueue(maxsize = 3)
stack.qsize() # 3

stack.put(1)
stack.put_nowait(2) # 1, 2
stack.full() # False

stack.get() # 2
stack.get_nowait() # 1
stack.empty() # True

q = Queue() # maxsize default to 0, which means an infinite queue
q.qsize() # 0

q.put(1)
q.put_nowait(2) # 1, 2
q.get() # 1
q.empty() # False
```

{% hint style="info" %}
A <mark style="color:yellow;">bounded queue</mark> can help to keep scarce resources under control in two ways:

1. By irreversibly rejecting elements that don’t fit
2. By overwriting the oldest element in the queue

【1】digital cameras support the [burst mode](https://en.wikipedia.org/wiki/Burst\_mode\_\(photography\)) for continuously shooting a series of pictures

【2】a basic <mark style="color:yellow;">cache</mark> that forgets the oldest element

Those two applications are design to release memory pressure.
{% endhint %}

## Pros and Cons

### **Advantages:**

* Stacks and Queues are <mark style="color:yellow;">efficient for adding and removing elements</mark>, as these operations have a time complexity of O(1).
* Stacks and Queues are designed for managing data <mark style="color:yellow;">in specific order</mark>.
* 【Stack】can be used to implement <mark style="color:yellow;">undo/redo functions</mark> in applications.
* 【Stack】is widely used for call <mark style="color:yellow;">traceback</mark>. This is usually a <mark style="color:yellow;">bounded</mark> stack, which you will find out during a stack overflow error caused by too many recursive calls.
* 【Stack】In compiled languages with static type checking, local variables are [allocated on the stack](https://en.wikipedia.org/wiki/Stack-based\_memory\_allocation), which is a fast memory region.
* 【Stack】can help detect unmatched brackets in a code block or evaluate arithmetic expressions represented in [reverse Polish notation (RPN)](https://en.wikipedia.org/wiki/Reverse\_Polish\_notation).&#x20;
* 【Stack】can help solve the [Tower of Hanoi](https://en.wikipedia.org/wiki/Tower\_of\_Hanoi) puzzle or keep track of the visited nodes in a [graph](https://en.wikipedia.org/wiki/Graph\_\(abstract\_data\_type\)) or a [tree](https://en.wikipedia.org/wiki/Tree\_\(data\_structure\)) traversed with the [depth-first search (DFS)](https://en.wikipedia.org/wiki/Depth-first\_search) algorithm.
* 【Queue】FIFO queue is the perfect tool for <mark style="color:yellow;">buffering data</mark> in streaming scenarios and for <mark style="color:yellow;">scheduling tasks</mark> that need to wait until some <mark style="color:yellow;">shared resource</mark> becomes available.
* 【Queue】on the other hand, can be used to traverse a tree in <mark style="color:yellow;">BFS</mark> order.

### **Drawbacks:**

* Stacks and Queues <mark style="color:yellow;">do not</mark> provide <mark style="color:yellow;">fast access</mark> to elements other than the top/end element.
* Stacks <mark style="color:yellow;">do not</mark> support <mark style="color:yellow;">efficient searching</mark>, as you have to pop elements one by one until you find the element you are looking for.

## Thread

{% hint style="danger" %}
you should never use `list` for any data structure that can be accessed by multiple threads. `list` is <mark style="color:red;">not thread-safe</mark>.

In general, you should use a <mark style="color:red;">`deque`</mark> if you’re not using threading. If you are using threading, then you should use a <mark style="color:red;">`LifoQueue`</mark>.
{% endhint %}

`deque` is a little more complex, however, it is clearly stated that both the `.append()` and `.pop()` operations are atomic, so if you restrict yourself to using only `.append()` and `.pop()`, then you will be thread safe.

Unlike `deque`, <mark style="color:yellow;">`LifoQueue`</mark> is designed to be <mark style="color:yellow;">fully thread-safe</mark>.

This full thread safety comes at a cost, however. To achieve this thread-safety, `LifoQueue` has to do <mark style="color:yellow;">a little extra work</mark> on each operation, meaning that it will take a little longer.

## Summary

1. `list` is usually not recommended to implement Stack or Queue, and it has <mark style="color:yellow;">reallocate</mark> issue.
2. `collections.deque` is <mark style="color:yellow;">flexible and fast</mark>, which can change the end during the runtime.
3. `queue` module is <mark style="color:yellow;">fully thread-safe</mark>, but slightly slower.
4. Stack or Queue is not recommended for frequently <mark style="color:red;">element searching</mark> or <mark style="color:red;">middle element accessing</mark>.
5. popular applications:&#x20;
   * <mark style="color:yellow;">undo/redo functions</mark>
   * function call <mark style="color:yellow;">traceback</mark>
   * detect unmatched brackets in a code block
   * evaluate arithmetic expressions
   * <mark style="color:yellow;">scheduling tasks of shared resources</mark>
   * DFS/BFS searching
   * [burst mode](https://en.wikipedia.org/wiki/Burst\_mode\_\(photography\)) of digital cameras
   * <mark style="color:yellow;">cache</mark> management
   * calculating the [moving average](https://en.wikipedia.org/wiki/Moving\_average) of pixel intensities
   * ...
6.

[^1]: <mark style="color:yellow;">double-ended queue(</mark>_<mark style="color:yellow;">deck</mark>_<mark style="color:yellow;">)</mark>
