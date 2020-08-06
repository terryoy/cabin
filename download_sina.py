import requests

"""
Examples for 163 blog requests:



"""

session = requests.Session()
headers = {
}

PARAM_TEMPLATE = {
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





