echo -e '\ntest_urllib.py' && time for x in {1..10}; do py3 test_urllib.py; done
echo -e '\ntest_urllib3.py' && time for x in {1..10}; do py3 test_urllib3.py; done
echo -e '\ntest_requests.py' &&  time for x in {1..10}; do py3 test_requests.py; done
echo -e '\ntest_aiohttp.py' && time for x in {1..10}; do py3 test_aiohttp.py; done
echo -e '\ntest_httpx.py' && time for x in {1..10}; do py3 test_httpx.py; done
