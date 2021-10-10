from urllib.request import urlopen
### import urllib

def func_url(base_url):
    return urlopen(base_url).getcode()

def test_answer():
    assert func_url('http://localhost:8080/sample') == 200
