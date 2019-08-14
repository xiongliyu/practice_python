#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import json

url = {
    'get': r'https://api.github.com/events',
    'post': r'http://httpbin.org/post',
    'put': r'http://httpbin.org/put',
    'delete': r'http://httpbin.org/delete',
    'head': r'http://httpbin.org/get',
    'options': r'http://httpbin.org/get'
}

# r = requests.get(url['get'])
# print(r.status_code)

# r1 = requests.post(url['post'], data = {'hello': 'liyu'})
# print(r1.status_code)

# r2 = requests.put(url['put'], data = {'hi': 'python'})
# print(r2.status_code)

# r3 = requests.delete(url['delete'])
# print(r3.status_code)


'''传递URL参数
1. 传递的参数会放到'?'后面, 多个参数使用'&'连接
2. 传递url参数使用params 关键字参数
3. 带参数url(查询字符串)的目的: 检索指定关键字内容
4. 字典值为None的建都不会被添加到URL的查询字符串里面
'''
# payload = {'key1': 'value1', 'hi': 'python'}
# payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
# r = requests.get("http://httpbin.org/get", params=payload)
# print(r.url)

'''res
r.text: 返回一个list[{},{},...]
r.content: 返回一个二进制 b'[{}, {}, ...]'
r.json(): 返回一个json数据[{},{},...] 注需要使用r.status_code先检查是否请求成功,失败也会返回json
r.raw: 获取原始响应内容,原始套接字, 需要加入:"stream=True"
'''
# r = requests.get(url['get'])
# print(r.encoding)
# r.encoding = 'ISO-8859-1'
# print(r.encoding)
# print(r.json())
# print(r.raise_for_status())
# print(r.status_code)
# r = requests.get('https://api.github.com/events', stream=True)
# print(r.raw.read(10))


'''定制请求头部
只需要在请求的时候添加一个dict给headers 就可以了
head的值必须是string
'''
# url = 'https://api.github.com/some/endpoint'
# headers = {'user-agent': 'my-app/0.0.1'}
#
# r = requests.get(url, headers=headers)



'''post
post可以像data传入一个元祖列表,

将dict 转为json : data.dumps()

向json 传递参数可以自动编码
'''

# 传入元祖,在多个value使用同一个key时比较好用
payload = (('key1', 'value1'), ('key1', 'value2'))
payload1 = {'some': 'data'}

# r = requests.post('http://httpbin.org/post', data=payload)
# print(r.text)

# r1 = requests.post('https://api.github.com/some/endpoint', data=json.dumps(payload1))
# print(r1.text)

r2 = requests.post('https://api.github.com/some/endpoint', json=payload1)
print(r2.text)




'''响应状态码
r.status_code :200
r.raise_for_status(): 4xx,5xx None
'''