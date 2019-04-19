# -*- coding: utf-8 -*-
# @Author: dell
# @Date:   2019-04-17 16:42:29
# @Last Modified by:   kzk
# @Last Modified time: 2019-04-19 16:22:18

def Bubble(arr):
	max_index = len(arr)-1
	for i in range(0,max_index):
		for j in range(0,max_index - i):
			if arr[j] > arr[j+1]:
					tmp = arr[j]
					arr[j] = arr[j+1]
					arr[j+1] = tmp
	return arr


def Insertion(arr):
	for i in range(1, len(arr)):
		tmp = arr[i]
		j = 0		
		for j in range(i-1,-2,-1):  
		#由于在java中判断j >=0 时满足条件会再-1，因此j的取值为-1，所以要到写至-2。
		#这个调了很久，都不知道为啥，原来是在-1这里。
			# print j
			if arr[j] > tmp:
				arr[j+1] = arr[j]						
			else:
				break
		arr[j+1] = tmp
	return arr



def Selection(arr):
	"""
	在选择最小的，
	"""
	for i in range(0, len(arr)-1):
		index = i
		min_val = arr[i]
		for j in range(i+1,len(arr)):
			if arr[j] < min_val:
				index = j
				min_val = arr[j]
		arr[index] = arr[i]
		arr[i] = min_val
	return arr




if __name__ == '__main__':
	arr = [15,9,2,1,13,5,10]
	# print Bubble(arr)
	# print Insertion(arr)
	print Selection(arr)

