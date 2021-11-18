#!/usr/bin/env python

import urllib2

def request_url():
    gh_url = 'https://api.github.com'
    req = urllib2.Request(gh_url)
    
    password_manager = urllib2.HTTPPasswordMgrWithDefaultRealm()
    password_manager.add_password(None, gh_url, 'user', 'pass')
    
    auth_manager = urllib2.HTTPBasicAuthHandler(password_manager)
    opener = urllib2.build_opener(auth_manager)
    
    urllib2.install_opener(opener)
    handler = urllib2.urlopen(req)
    
    print(handler.getcode())
    print(handler.headers.getheader('content-type'))
    
def main():
    request_url()
    
if __name__ == "__main__":
    main()