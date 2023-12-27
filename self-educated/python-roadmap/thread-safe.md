# Thread-Safe

## Logging

You can use the [`print()`](https://realpython.com/python-print/) function in asynchronous code because everything runs on a single thread. On the other hand, you’d have to replace it with the [`logging`](https://realpython.com/python-logging/) module in a multithreaded code because the `print()` function isn’t thread-safe.

## Queue

`queue` module is thread-safe, while `list` or `deque` is not.
