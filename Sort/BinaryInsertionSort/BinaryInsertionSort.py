# -*- coding: utf-8 -*-
#ASC
# Binary Insertion Sort
def binInsertSort(slist):
	for i in range(2, len(slist)):
		slist[0] = slist[i]
		low = 1
		high = i - 1
		while low <= high:
			mid = (low + high) / 2
			if slist[0] < slist[mid]:
				high = mid - 1
			else:
				low = mid + 1
		j = i - 1
		while j >= high + 1:
			slist[j + 1] = slist[j]
			j = j - 1
		slist[high + 1] = slist[0]
	print slist