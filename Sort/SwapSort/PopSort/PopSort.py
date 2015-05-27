# -*- coding: utf-8 -*-

#冒泡排序 升序
def popSwapSortASC(slist):
	for i in range(len(slist)):
		for j in range(1, len(slist) - i):
			if slist[j] < slist[j - 1]:
				slist[j - 1], slist[j] = slist[j], slist[j - 1]
	print slist

#冒泡排序 降序	
#在python里面这个是多余的，因为可以直接调用slist.reverse()方法
def popSwapSortDSC(slist):
	for i in range(len(slist)):
		for j in range(1, len(slist) - i):
			if slist[j] > slist[j - 1]:
				slist[j - 1], slist[j] = slist[j], slist[j - 1]
	print slist
			
