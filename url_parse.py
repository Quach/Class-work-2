# -*- coding: utf-8 -*-
"class work 2"

import urllib2

def get_page(source_url):
    "Get page as a string from url"

    req = urllib2.Request(source_url)
    res = urllib2.urlopen(req)
    page = res.read()

    return page

def get_urls(source_page, main_url, level):
    "Return an array of urls with leves not more than sets"

    res_urls = []
    while 1:
        begin_url = 0
        end_url = 0
        begin_url = source_page.find('"http://')
        if begin_url == -1:
            break
        end_url = source_page[begin_url + 1:].find('"')
        if end_url == -1:
            break
        temp_url = source_page[begin_url + 1: end_url + begin_url + 1].split('://')[1]
        if len(temp_url.split('/')) <= level + 1:
            if temp_url.split('/')[0] == main_url:
                res_urls.append(source_page[begin_url + 1: end_url + begin_url + 1])
        source_page = source_page[end_url + begin_url + 2:]
    return res_urls

def get_links(url, level):
    "main function"

    main_url = url.split('://')[1].split('/')[0]
    return get_urls(get_page(url), main_url, level)

def main():
    "main"

    print get_links('http://www.google.com.ua/', 1)
    raw_input()
    return 0

if __name__ == "__main__":
    exit(main())
