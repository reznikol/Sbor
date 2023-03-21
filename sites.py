#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sqlite3
from urllib.parse import urlsplit


DIRECTORY = 'Files'


def walk(directory):
    s = set()
    for root, dirs, files in os.walk(directory):
        for name in files:
            new_frequency = sql_work(os.path.join(root, name))
            s = s | new_frequency
    save_result(s)  
            

def sql_work(file):
    conn = sqlite3.connect(file)
    cursor = conn.cursor()
    results = cursor.execute("SELECT url FROM urls").fetchall()
    conn.close()
    return pars_url(results)


def pars_url(spis):
    flatten = [str(item) for sub in spis for item in sub]
    s = set()
    for i in range(len(flatten)):
        url = urlsplit(flatten[i])
        if url.scheme == 'file':
            None
        elif url.scheme == 'https' or 'http':
            s.add(url.netloc)
    return s
    

def save_result(s):
    s = list(s)
    f = open('hosts.txt','w')
    for i in range(len(s)):
        f.write('127.0.0.1' + ' ' + s[i] + '\n')
    f.close()


if __name__ == '__main__':
    walk(DIRECTORY)
