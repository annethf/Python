# -*- coding: utf-8 -*- 

def insertSort(slist):
	for i in range(2, len(slist)):
		if slist[i] < slist[i - 1]:
			slist[0] = slist[i]
			slist[i] = slist[i - 1]
			j = i - 2
			while slist[0] < slist[j]:
				slist[j + 1] = slist[j]
				j = j - 1
			slist[j + 1] = slist[0]
	print slist