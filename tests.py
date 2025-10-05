import requests


resp = requests.get("http://0.0.0.0:8181/ping/")

assert resp.text == '<html>\n    status: ok\n</html>'

assert 200 <= resp.status_code < 300