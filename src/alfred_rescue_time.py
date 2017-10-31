#!/usr/bin/python

__author__ = 'vincent yang'

# Constant paths
base = 'https://www.rescuetime.com/'
dash_path = 'dashboard'
api_path = 'anapi/manage'
weekly_path = 'dashboard/for/the/week/of/'
monthly_path = 'dashboard/for/the/month/of/'
yearly_path = 'dashboard/for/the/year/of/'

# Functions
# 1. Open up different links to dash, daily, monthly, yearly
# 2. Set API key, view graphs
# 3. Get n most frequent events
# 4. Get Focused

import sys
import subprocess   # used for running bash commands
import os           # used for accessing env variables
import requests     # used for API requests
import datetime
import pyperclip
from plistlib import readPlist, writePlist

info = readPlist('info.plist')
now = datetime.datetime.now()

"""
Run a linux command
"""
def shell(command):
    if not isinstance(command, list):
        command = [command]
    subprocess.check_output(command)

"""
url should be a list of arguments
Example: url = ['ls', '-al']
"""
def open(url):
    if not isinstance(url, list):
        url=[url]
    shell(['open'] + url)

    
if __name__ == '__main__':
    query = sys.argv[1]
    date = now.strftime("%Y-%m-%d")
    
    # Open dash
    if query[0] == 'd':
        p = base + dash_path
        open(p)
    # Weekly view
    elif query[0] == 'w':
        p = base + weekly_path + date
        open(p)
    # Monthly view
    elif query[0] == 'm':
        p = base + monthly_path + date
        open(p)
    # Yearly view
    elif query[0] == 'y':
        p = base + yearly_path + date
        open(p)

    # Not currently functional
    #elif query == 'api':
    #    # check if file exists
    #    if 'RESCUETIME_API_KEY' in info['variables']:
    #        sys.stderr.write(info['variables']['RESCUETIME_API_KEY'])
    #        sys.stderr.write("lalala")
    #    else:
    #        sys.stderr.write("No key")
    #        sys.stderr.write(str(info['variables']))
    #        p = base + api_path
    #        open(p)
            
    # Set api key
    #elif query == 'set': 
    #    new_api_key = sys.argv[2]
    #    print("new api key is " + str(new_api_key))
    #    info['variables']['RESCUETIME_API_KEY'] = str(new_api_key)
    #    sys.stderr.write(str(info['variables']))
    #    writePlist(info, 'info.plist')

    # Open up graphs
    elif query == 'graph' or query[0] == 'g':
        # Change clipboard to API key
        # Open link
        p = 'http://ilbonte.github.io/rescuetime-again/'
        if 'RESCUETIME_API_KEY' in info['variables']:
            pyperclip.copy(info['variables']['RESCUETIME_API_KEY'])

        open(p)
    # Get focused
    #elif query == 'gf' or query == 'focus':
    #    pass

    ## string is number
    #elif query.isdigit():
    #    # Use API to get n most recent events
    #    pass

    # by default, open dash
    else:
        p = base + dash_path
        open(p)

