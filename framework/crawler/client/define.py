# -*- coding: utf-8 -*-

# 定义client所需要的东西

class ContentType:
    RSS = 'rss'
    XML = 'xml'
    HTML = 'html'

class ClientType:
    FILE = 'file'
    REQUEST = 'request'


class CrawlerClient(object):
    entry = None
    content = None

    def set_entry(self, entry_url):
        self.entry = entry_url

    def get(self):
        """返回第一部分内容"""
        return None

    def next(self):
        return None



class FileCrawlerClient(CrawlerClient):

    def get(self):
        if not self.entry:
            raise RuntimeError('entry is not defined.')

        with open(self.entry, 'r') as f:
            self.content = f.read()

        return self.content




# 获取一个可以
def create_client(client_type):
    if client_type == ClientType.FILE:
        return FileCrawlerClient()
    elif client_type == ClientType.REQUEST:
        pass
    else:
        raise RuntimeError('Unknown client type: {}'.format(client_type))
