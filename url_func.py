# -*- coding: utf-8 -*-
"class work 2"

def urlparse(source_url):
    "Parsing url adress"

    parsed_url = {}
    temp = []
    parsed_url['scheme'] = ''
    parsed_url['username'] = ''
    parsed_url['password'] = ''
    parsed_url['domain'] = ''
    parsed_url['port'] = ''
    parsed_url['path'] = ''

    #divide schema and domain
    temp = source_url.split('://')
    parsed_url['scheme'] = temp[0]

    #devide domain and path
    temp = temp[1].split('/')
    if len(temp) >= 2:
        for i in temp[1:]:
            parsed_url['path'] += '/' + i 

    #devide username and domain
    temp = temp[0].split('@')

    if len(temp) != 1:
        #user pass
        if len(temp[0].split(':')) > 1:
            #user pass and something ERROR!
            if len(temp[0].split(':')) > 2:
                return None
            parsed_url['password'] = temp[0].split(':')[1]
            if parsed_url['password'] == '':
                return None
        parsed_url['username'] = temp[0].split(':')[0]
        if parsed_url['username'] == '':
            return None
        #sen domani name
        temp = temp[1].split(':')

    if len(temp) != 1:
        #domain and port and something ERROR!
        if len(temp) > 2:
            return None
        parsed_url['port'] = temp[1]
        if parsed_url['port'] == '':
            return None

    #just domain name
    parsed_url['domain'] = temp[0]
    if parsed_url['domain'] == '':
        return None

    return parsed_url

def main():
    "main"

    #print urlparse('http://quach:jennifer@google.com:8080/a/b')
    assert urlparse('http://quach:jennifer@google.com:8080/a/b') == {'scheme' : 'http', 'username' : 'quach', 'password' : 'jennifer', 'domain' : 'google.com', 'port' : '8080', 'path' : '/a/b'}
    assert urlparse('http://google.com/a/b') == {'scheme' : 'http', 'username' : '', 'password' : '', 'domain' : 'google.com', 'port' : '', 'path' : '/a/b'}
    assert urlparse('http://quach::@google.com:8080/a/b') == None
    assert urlparse('http://:jennifer@google.com:8080/a/b') == None
    assert urlparse('http://jennifer@google.com:8080/a/b') == {'scheme' : 'http', 'username' : 'jennifer', 'password' : '', 'domain' : 'google.com', 'port' : '8080', 'path' : '/a/b'}
    assert urlparse('http://quach:jennifer:@8080/a/b') == None
    assert urlparse('http://quach:jennifer@8080:/a/b') == None
    print 'TEST OK!'

    #raw_input()
    return 0


if __name__ == "__main__":
    exit(main())
