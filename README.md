# request-
request参数快速调整
使用的方法，比如这是：
cookies={}
headers={}
params={}
url ='https://api.bilibili.com/x/v3/fav/resource/list'
optimizer = RequestOptimizer(url, tolerance=100, params=params, headers=headers, cookies=cookies)
# 优化请求参数和 headers
optimizer.main()
判断的方法是can_remove_key()里面，如果要修改增加自己的方法可以在里面修改，目前采用的是数值计算，判断返回值的长度 tolerance为大小区间，这个区间必须有，服务器返回的数据会因为请求头的改变而微变，这个值具体多少一般最多300就够了
