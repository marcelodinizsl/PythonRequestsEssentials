#!/usr/bin/env python

import requests

def request_url():
    result = requests.get('https://api.github.com', auth=('user','pass'))
    
    print(result.status_code)
    print(result.headers['content-type'])
    
def main():
    request_url()
    
if __name__ == "__main__":
    main()