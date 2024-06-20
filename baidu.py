import requests
from as_module import RequestOptimizer

# 定义初始参数和 headers
params = {
    'param1': 'value1',
    'param2': 'value2'
}
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'origin': 'https://space.bilibili.com',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
}

url = 'https://baidu.com'

# 创建 RequestOptimizer 对象
optimizer = RequestOptimizer(url, tolerance=300, params=params, headers=headers)
# 优化请求参数和 headers
optimized_dicts = optimizer.main()

