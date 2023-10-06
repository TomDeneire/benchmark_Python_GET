echo 'test_urllib.py' && time for x in {1..10}; do py3 test_urllib.py; done
echo 'test_urllib3.py' && time for x in {1..10}; do py3 test_urllib3.py; done
echo 'test_requests.py' &&  time for x in {1..10}; do py3 test_requests.py; done
echo 'test_aiohttp.py' && time for x in {1..10}; do py3 test_aiohttp.py; done
echo 'test_httpx.py' && time for x in {1..10}; do py3 test_httpx.py; done
