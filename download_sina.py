import requests

from framework.utils.dwr_client import DWRClient

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

PARAM_1 = {
	"callCount": 1,
#	"scriptSessionId": "${scriptSessionId}187",
#	"c0-scriptName": "BlogBeanNew",
#	"c0-methodName": "getBlogs",
	"c0-id": 0,
#	"c0-param0": "number:61512981",
#	"c0-param1": "number:0",
#	"c0-param2": "number:20",
#	"batchId": 820803
}

def main():
    HOST = 'http://api.blog.163.com'
    PAGE = '/terryoy/dwr/call/plaincall/BlogBeanNew.getBlogs.dwr'
    dwr = DWRClient(requests.Session(), HOST)
    dwr.set_params(PARAM_1)
    dwr.set_page(PAGE)
    dwr.init()
    
    res = dwr.request('BlogBeanNew', 'getBlogs', [ '61512981', '20', '0'])
    print(res.content)








if __name__ == '__main__':
    main()





