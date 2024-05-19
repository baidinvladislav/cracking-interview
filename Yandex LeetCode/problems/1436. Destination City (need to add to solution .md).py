from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        paths_dict = {}

        for from_city, to_city in paths:
            paths_dict[from_city] = to_city

        for val in paths_dict.values():
            if val not in paths_dict:
                return val
