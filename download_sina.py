import requests
"""
Examples for sina blog requests:


http://blog.163.com/regulator/api/blog/moveBlogName?userName=terryoy


http://api.blog.163.com/terryoy/dwr/call/plaincall/BlogBeanNew.getBlogs.dwr
第一页请求：
callCount=1
scriptSessionId=${scriptSessionId}187
c0-scriptName=BlogBeanNew
c0-methodName=getBlogs
c0-id=0
c0-param0=number:61512981
c0-param1=number:0
c0-param2=number:20
batchId=820803

第二页请求：
callCount=1
scriptSessionId=${scriptSessionId}187
c0-scriptName=BlogBeanNew
c0-methodName=getBlogs
c0-id=0
c0-param0=number:61512981
c0-param1=number:20
c0-param2=number:10
batchId=324598

"""

session = requests.Session()
headers = {
    "Referer": "http://api.blog.163.com/crossdomain.html?t=20100205",
	"Content-Type": "text/plain",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
}

PARAM_TEMPLATE = {
    "callCount": 1,
    "scriptSessionId": "${scriptSessionId}187",
    "c0-scriptName": "BlogBeanNew",
    "c0-methodName": "getBlogs",
    "c0-id": 0,
    "c0-param0": "number:61512981",
    "c0-param1": "number:0",
    "c0-param2": "number:20",
    "batchId": 820803
}

def post(offset=0, limit=20):
    HOST = 'http://api.blog.163.com'
    PAGE = '/terryoy/dwr/call/plaincall/BlogBeanNew.getBlogs.dwr'
    url = HOST + PAGE
    data = PARAM_TEMPLATE
    data["c0-param1"] = "number:" + str(offset)
    data["c0-param2"] = "number:" + str(limit)

    print('request:', url, data, headers)
    res = session.post(url, data=data, headers=headers)
    return res.content.decode('gbk')

def main():
    content = post()
    print('content:', content)






if __name__ == '__main__':
    main()





