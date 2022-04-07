class Solution:
	def sortArray(self, nums: List[int]) -> List[int]: 

		def MergeSort(nums):
			n = len(nums)
			if n <= 1: return nums
			mid = n//2

			l = MergeSort(nums[:mid])
			r= MergeSort(nums[mid:])
			merge = [0]*n

			if not l:return r
			if not r:return l

			ni, mi = len(l), len(r)
			i, p , j = 0, 0 ,0 

			while p < n:
				if not j < mi: 
					merge[p] = l[i]
					i += 1
				elif not i < ni: 
					merge[p] = r[j]
					j += 1
				elif l[i] < r[j]:
					merge[p] =l[i]
					i += 1
				else:
					merge[p] = r[j]
					j += 1
				p += 1
			return merge

		return MergeSort(nums)
