# -*- coding: utf-8 -*-
# @Author: dell
# @Date:   2019-04-17 16:42:29
# @Last Modified by:   kzk
# @Last Modified time: 2019-04-17 16:56:24

def Bubble(arr):
	max_index = len(arr)-1
	for i in range(0,max_index):
		for j in range(0,max_index - i):
			if arr[j] > arr[j+1]:
					tmp = arr[j]
					arr[j] = arr[j+1]
					arr[j+1] = tmp
	return arr





if __name__ == '__main__':
	arr = [11,7,4,3,5,2,0,8,9,1,99,2]
	print Bubble(arr)