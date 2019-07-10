

# 并发编程之Futures





- 并行与并发



![img](https://static001.geekbang.org/resource/image/37/3f/37cbce0eb67909990d83f21642fb863f.png)

 并发，是指遇到I/O阻塞时（一般是网络I/O或磁盘I/O），通过多个线程之间切换执行多个任务（多线程）或单线程内多个任务之间切换执行的方式来最大化利用CPU时间，但同一时刻，只允许有一个线程或任务执行。适合I/O阻塞频繁的业务场景。

并发操作可以看做是对CPU资源的压榨，主要适合I/O 频繁的操作，由于I/O操作时间比CPU运行时间长造成CPU空闲，因此为避免CPU资源浪费，通过多线程可以切换到到其他任务执行，进而实现CPU的充分利用（压榨~！）。其实只占用一个CPU核心。

对于Intel多核心，每个核心有两个线程。

![ae88578de4b2d785df806000aac922f.png](https://i.loli.net/2019/07/09/5d2435b9cb24c85207.png)

所以根据6核处理器，则有12个系统线程数。

所以并不是线程数越多越好，当线程数=系统自由线程数时。当线程数大于系统自由线程数时，线程切换的开销是很大的。

![img](https://static001.geekbang.org/resource/image/f6/3c/f6b4009c8a8589e8ec1a2bb10d4e183c.png)

并行适合CPU heavy的场景，MapReduce中的并行计算可以加快运行速度。由于并行CPU的每个核都充分利用，所以是CPU多核心同时工作的。

并行，是指多个进程完全同步同时的执行。适合CPU密集型业务场景。  



- 并发的多线程实现

```python
import concurrent.futures
import requests
import threading
import time

def download_one(url):
    resp = requests.get(url)		#线程安全
    print('Read {} from {}'.format(len(resp.content), url))

def download_all(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_one, sites)

def main():
    sites = [
        'https://en.wikipedia.org/wiki/Portal:Arts',
    ]
    download_all(sites)
if __name__ == '__main__':
    main()
```

多线程通过concurrent.futures模块实现，共有5个线程可以分配使用。





```python
#多线程
with futures.ThreadPoolExecutor(workers) as executor
=>
#多进程
with futures.ProcessPoolExecutor() as executor: 
```

多进程通常情况下，workers省略，系统自动返回。



Futures模块：concurrent.futures 和 asyncio中。均表示带有延迟的操作。源码中解释为：表示异步计算的结果。

Futures会将处于等待状态的操作包裹起来放在队列里，这些操作的状态可以随时查看。

- Executor类：executor.submit (func) 便会安排func函数执行，并返回一个future实例
- future.add_done_callback(fn)：Futures完成后通知回调函数fn执行
- concurrent.futures.as_completed(fs) 针对给定的future迭代器fs，返回完成后的迭代器
- future.result( ) 表示future完成后，返回结果或者异常







> 评论区

老师好，请问一下在python存在GIL的情况下，多进程是不是还是无法并发运行？谢谢老师

作者回复: 如果是多进程，则无所谓，可以并发运行。GIL是作用在线程上的，是不允许进程中的多线程同时运行

