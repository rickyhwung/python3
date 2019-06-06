import urllib, urllib3, zlib
from io import StringIO
from gzip import GzipFile
from urllib import request

def loadData(url):
    request1 = urllib.request.urlopen(url)
    request1.add_header('Accept-encoding', 'gzip,deflate')
    response = url(request1)
    content = response.read()
    encoding = response.info().get('Content-Encoding')
    if encoding == 'gzip':
        content = gzip(content)
    elif encoding == 'deflate':
        content = deflate(content)
    return content

def gzip(data):
    buf = StringIO(data)
    f = gzip.GzipFile(fileobj=buf)
    return f.read()

def deflate(data):
    try:
        return zlib.decompress(data, -zlib.MAX_WBITS)
    except zlib.error:
        return zlib.decompress(data)

def main():
    url = "http://www.chinapost.com.cn/html1/category/181312/8238-1.htm"
    content = loadData(url)
    print(content)

if __name__ == '__main__':
    main()

header = {
    'Host': 'www.chinapost.com.cn',
    'If-None-Match': 'E95AE5D074FFC0026BEB20217A5FEFBE'
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}