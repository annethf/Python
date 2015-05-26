# -*- coding: utf-8 -*-
 
def seqSearch(slist, key):
	slist[0] = key
	for i in range(1, len(slist)):
		if slist[i] == slist[0]:
			return i
	return 0