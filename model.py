#!/usr/bin/env python
# coding=utf-8
import web, datetime

db = web.database(dbn='mysql', db='chaoge', user='root', pw='')

def get_lists():
	return db.select('lists', order='id DESC')

def get_alist(id):
	try:
		return db.select('lists', where='id=$id', vars=locals())[0]
	except IndexError:
		return None

def new_alist(title, text):
	db.insert('lists', title=title, content=text, listed_on=datetime.datetime.utcnow())