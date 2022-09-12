"""
Given an integer array nums and an integer k, return the k most 
frequent elements. You may return the answer in any order.
"""



class Solution:
    def top_k_frequent(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ### Solution 1 ###
        # d = {}
        # response = []

        # for i in nums:
        #     if i not in d:
        #         d[i] = [i]
        #     else:
        #         d[i].append(i)

        # while k > 0:
            # max -> the function that grabs the biggest value
            # d -> dictionary, it iterates through and grabs each key
            # key -> overrides the default behavior of the max function
            # lambda x -> defines a lambda to handle new behavior of max
            # d[x] -> the list defined by key 'x'
        #     max_key = max(d, key = lambda x: len(list(d[x])))
        #     response.append(max_key)
        #     d.pop(max_key)
        #     k -= 1
        
        # return response


        ### Solution 2 ###
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        arr = sorted(d.keys(), key = d.get, reverse=True)

        return arr[:k]



    nums = [1,1,1,2,2,3]
    k = 2
    # nums = [3,0,1,0]
    # k = 1
    top_k_frequent(nums, k)