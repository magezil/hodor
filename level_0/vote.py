#!/usr/bin/python3
"""This module votes for id 256 1024 times"""
import requests

for i in range(1024):
    r = requests.post('http://158.69.76.135/level0.php', data={'id':'256', 'holdthedoor':'submit'})
