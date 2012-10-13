# -*- coding: utf-8 -*-
"class work 2"

def join(source_url, add_path):
    "Joinning urls fro some options"

    res_url = source_url

    if add_path.find('://') == -1:
        #old url
        if add_path[0] == '/':
            #new path
            res_url = source_url.split('://')[1]
            res_url = res_url.split('/')[0]
            res_url = source_url.split('://')[0] + '://' + res_url + add_path
        else:
            #continue path
            res_url = source_url + '/' + add_path
    else:
        #new URl
        res_url = source_url.split('://')[1]
        temp = ''
        for i in res_url.split('/')[1:]:
            temp += '/' + i
        res_url = add_path + temp

    return res_url

def main():
    "main"

    assert join('http://google.com/x', 'a/b/c') == 'http://google.com/x/a/b/c'
    assert join('http://google.com/x', '/a/b/c') == 'http://google.com/a/b/c'
    assert join('http://google.com', 'a/b/c') == 'http://google.com/a/b/c'
    assert join('http://google.com', '/a/b/c') == 'http://google.com/a/b/c'

    assert join('http://google.com/x', 'http://yandex.com') == 'http://yandex.com/x'
    assert join('http://google.com', 'http://yandex.com') == 'http://yandex.com'
    assert join('http://google.com', 'http://yandex.com/x') == 'http://yandex.com/x'
    assert join('http://google.com/x/a/d', 'http://yandex.com') == 'http://yandex.com/x/a/d'

    print "TEST OK!"
    return 0


if __name__ == "__main__":
    exit(main())
