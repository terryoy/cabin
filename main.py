from config import site
from bs4 import BeautifulSoup
from datetime import datetime
import os
import html2text

from framework.crawler.client import create_client
from framework.utils import dateutils
from framework.utils import fileutils


def post_parser(entry):
    result = {
        "title": entry.title.text,
        "publishtime": entry.publishtime.text,
        "modifytime": entry.modifytime.text,
        "content": entry.content.text
    }
    return result

def get_export_file_name(post):
    return "./output/archive/{}-{}.md".format(
        post["publishtime"],
        post["title"]
    )

def get_export_file_content(post):
    convertor = html2text.HTML2Text()
    template = """---\n layout: post\n title: {}\n date: {}\n tags: {}\n---\n{}"""
    return template.format(
        post["title"],
        dateutils.from_timestamp(float(post["publishtime"])).strftime('%Y-%m-%d %H:%M'),
        u"旧博客存档",
        convertor.handle(post["content"])
    )

def export_post(post, idx):
    path = get_export_file_name(post)
    fileutils.ensure_path(os.path.dirname(path))

    with open(path, 'w') as f:
        f.write(get_export_file_content(post))
        f.flush()


def main():

    # get content
    client = create_client(site.SITE_CLIENT)
    client.set_entry(site.SITE_ENTRY)

    # parse
    content = client.get()
    doc = BeautifulSoup(content)

    # export
    postNodes = doc.find_all('postitem')

    idx = 1
    for p in reversed(postNodes):
        post = post_parser(p)
        export_post(post, idx)
        idx += 1


if __name__ == '__main__':
    main()
