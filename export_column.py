#!/bin/python

import sqlite3
import argparse
import json

ap = argparse.ArgumentParser()
ap.add_argument("-q", "--query", required=True,
	help="destination")
ap.add_argument("-c", "--column", required=True,
	help="column")
ap.add_argument("-i", "--index",
	help="index")
ap.add_argument("-o", "--output",
	help="output line or list",default="line")
args = vars(ap.parse_args())

# Init Database
con = sqlite3.connect('nums.db')
con.row_factory = sqlite3.Row
c = con.cursor()

c.execute(args['query'])
rows = c.fetchall()
result=""
for row in rows:
        value = row[args['column']]
        if args['index']:
            array=json.loads(value)
            value = array[int(args['index'])]



        if 'line' in args['output']:
            result += f"{value}\n"
        else:
            result += f",{value}"


if 'list' in args['output']:
    result = result[1:]

print(result)
con.close()
