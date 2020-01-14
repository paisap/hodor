#!/usr/bin/python3
import requests
print("se esta compilando we")
for i in range(1023):
    requests.post('http://158.69.76.135/level0.php', data={'id': '1186', 'holdthedoor': 'submit'})
print("se compilo we")
