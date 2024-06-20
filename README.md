# request-

request参数快速调整的方法

### 作用：

我们都知道在requset的使用中使用快速复制浏览器参数的方法获得的最后信息特别庞大，需要取筛选哪些是必须的，as_moudle就是用自动化完成这一部分的模块。

### 示例（baidu.py是一个完整的项目示例）：

使用的方法，比如这是一段示例：

```python
import requests
from as_module import RequestOptimizer
cookies={}
headers={}
params={}
url ='.com'
optimizer = RequestOptimizer(url, tolerance=100, params=params, headers=headers, cookies=cookies)
headersoptimizer.main()
```

tolerance=100是判断返回数值的改变的区间，原理是正常返回和报错返回的信息量大小不一样。一般最多300就够了，理论上越大越好，但是超过初始返回值就没有意义了。如果是网站的返回值特别小或者正确返回值（初始参数）和错误返回值特别接近，可能需要can_remove_key()自己重写判断逻辑，比如关键字识别等，

### 未完善的地方（计算量特别大时）：

#### 1，建立线程池或者协程

可以对各个类都写进去，这样不要的可以取消，现在只能全部一起验证

#### 2，单独写每个参数的输入

目前使用的是**kwargs，没有对headers等做单独的识别， 所以只能验证所有参数而不能跳过

#### 3，可以写算法来提升效率

#### 4，加入ip更换

这个不会，算了

### 可能导致的问题：

访问量特别敏感的网站慎用，可能被ban
