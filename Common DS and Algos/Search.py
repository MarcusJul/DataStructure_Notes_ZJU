#
def binary_search(lst, target):
	
	left, right = 0, len(lst)-1
	flag = False
	while(left<=right and not flag):
		mid = (left+right)//2
		if lst[mid] == target:
			flag = mid
		else:
			if target < lst[mid]:
				right = mid - 1
			else:
				left = mid + 1

	return flag