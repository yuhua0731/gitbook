---
description: aka priority queue
---

# Heap

## Basic definitions:

* heap is a tree-based data structure, values/keys in heaps do **not** have to be unique
* max heap - parent node always has a <mark style="color:blue;">greater or equal</mark> value than children
* min heap - parent node always has a <mark style="color:blue;">smaller or equal</mark> value than children
* in python, heap is always min heap, 0-indexed, `pq[0]` is the minimum element

## General functions:



<table data-full-width="true"><thead><tr><th width="336">Operation</th><th width="462">Description</th><th>Time complexity</th></tr></thead><tbody><tr><td><code>heapq.heappush(pq, key)</code></td><td>inserts <code>key</code> into heap</td><td><code>O(log n)</code></td></tr><tr><td><code>heapq.heappop(pq)</code></td><td>removes and returns the minimum <code>key</code> from heap</td><td><code>O(log n)</code></td></tr><tr><td><code>pq[0]</code></td><td>gets the minimum <code>key</code> of heap, will not remove it</td><td><code>O(1)</code></td></tr><tr><td><code>heapq.heapify(list)</code></td><td>generates a new heap from a list</td><td><code>O(n log n)</code></td></tr><tr><td><code>heapq.heappushpop(pq, key)</code></td><td>push <code>key</code> into heap than remove the minimum one</td><td><code>O(log n)</code></td></tr></tbody></table>

* **push/pop:** heap will be re-ordered during insertion or removal. Time complexity is <mark style="color:green;">`O(log n)`</mark> for `heapq.heappush` & `heapq.heappop`
* **peak:** in all conditions, `pq[0]` is the minimum element. `peak` has time complexity of <mark style="color:green;">`O(1)`</mark>
* **heapify:** the implementation is create an empty heapq, then insert all elements one by one. Thus, the time complexity of heapifying a heap is <mark style="color:green;">`O(n log n)`</mark>

> `heapq.heapify()` 是 Python 中用于将一个列表（或类似可迭代对象）转化成堆的方法。它的时间复杂度为 O(n)，其中 n 是列表的长度。
>
> 具体来说，`heapify()` 方法会对给定的列表进行原地操作，将其转化为一个符合堆的结构，不会返回新的堆对象。在堆化的过程中，它会从列表的中间位置开始向前遍历，对每一个非叶子节点执行下沉操作（调整堆的结构，保证堆的性质），最终得到一个堆。
>
> 这种操作的时间复杂度是 O(n)，因为只需要对大约一半的元素执行下沉操作，而下沉操作的时间复杂度是 O(log n)。因此，总的时间复杂度为 O(n log n)。

{% hint style="warning" %}
Note:

* heap is an implementation of binary tree. in python heapq's implementation, the indices of parent and children are linked with specific rules.&#x20;
* python use list-like approach to use heapq, note that the list is not ordered in increasing order entirely, which is, pq\[3] is not the forth smallest element.
* To define customized order rule, you can create a class and implement <mark style="color:blue;">`__lt__(self, other)`</mark>
{% endhint %}

## Sample

{% code lineNumbers="true" %}
```python
pq = [4, 3, 5]
heapq.heapify(pq)
pq[0] # 3
smallest_element = heapq.heappop(pq) # 3

heapq.heappush(pq, 1)
heapq.heappush(pq, 2)

smallest_element = heapq.heappop(pq) # 1
```
{% endcode %}

## How to use heap in algorithms

### minimum distance path in graph

* [Dijkstra's algorithm](https://app.gitbook.com/o/Mn9MdOeo1gYqJ3t2eDyE/s/CQCTmD2dmvBk81v6yd7L/\~/changes/7/algorithms/dijkstras-algorithm) - one critical part is to repeatedly extract the closest node from an unvisited node set, which is a minimum calculation.
* Event scheduler - find the next earliest event from day i (key is start timestamp in some situations, or end timestamp in some other situations).
* Running median - two heaps: one max heap to store the smaller half values, one min heap to store the greater half values. when a new value is inserted, we first push it into max heap, if the size of two heaps differ by more than 1, pop one from max heap and push it into min heap.

## **Strengths and Weaknesses**

### **Strengths**

* A min-heap is able to <mark style="color:yellow;">quickly extract</mark> the minimum value on the heap. Repeated extractions from a min-heap into an array will yield a sorted array.

### **Weaknesses**

* There's <mark style="color:yellow;">no convenient way of searching</mark> for a particular `key` value in a heap. Entries are only <mark style="color:yellow;">partially ordered</mark>.

{% hint style="success" %}
Heap or PriorityQueue is a good data structure for incoming <mark style="color:yellow;">message processing</mark> queue, when some messages have a higher priority, which some has a lower one.

In <mark style="color:yellow;">Robot movement control</mark>, emergency stop usually has the highest priority, while position update is much lower. In this case, we could use heap to cache the incoming messages.

for example, for each type of messages, we assign a priority number to it, and heappush elements like <mark style="color:yellow;">`(priority = 0, msg = emergency stop) or (priority = 3, msg = position update)`</mark>.&#x20;

In this way, we can ensure that the message with the highest priority will be processed first.
{% endhint %}

