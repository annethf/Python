# -*- coding: utf-8 -*-

def binSearchASC(slist, key):
	low = 0
	high = len(slist) - 1
	mid = 0
	while low <= high:
		mid = (low + high) / 2
		if slist[mid] == key:
			return mid
		if slist[mid] < key:
			low = mid + 1
		else:
			high = mid - 1
	return -1 

def binSearchDSC(slist, key):
	low = 0
	high = len(slist) - 1
	mid = 0
	while low <= high:
		mid = (low + high) / 2
		if slist[mid] == key:
			return mid
		if slist[mid] > key:
			low = mid + 1
		else:
			high = mid - 1
	return -1
		
