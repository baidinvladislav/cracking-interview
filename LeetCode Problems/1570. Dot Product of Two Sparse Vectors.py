"""
Given two sparse vectors, compute their dot product.

Implement class SparseVector:

SparseVector(nums) Initializes the object with the vector nums
dotProduct(vec) Compute the dot product between the instance of SparseVector and vec
A sparse vector is a vector that has mostly zero values,
you should store the sparse vector efficiently and compute the dot product between two SparseVector.

Follow up: What if only one of the vectors is sparse?
"""
from typing import List


class SparseVector:
    def __init__(self, nums: List[int]):
        self.v = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        n = len(vec.v)
        j = 0
        sum = 0
        for i in range(n):
            comp = self.v[i] * vec.v[j]
            sum += comp
            j += 1
        return sum


nums1 = [1, 0, 0, 2, 3]
nums2 = [0, 3, 0, 4, 0]

v1 = SparseVector(nums1)
v2 = SparseVector(nums2)
print(v1.dotProduct(v2))
