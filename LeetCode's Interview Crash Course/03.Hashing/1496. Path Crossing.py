# Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east,
# or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

# Return true if the path crosses itself at any point, that is, if at any time you are on a location you
# have previously visited. Return false otherwise.

# Example 1:
# Input: path = "NES"
# Output: false
# Explanation: Notice that the path doesn't cross any point more than once.

# Example 2:
# Input: path = "NESWW"
# Output: true
# Explanation: Notice that the path visits the origin twice.


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        points = [0, 0]

        s = set()
        for dest in path:
            s.add(tuple(points))

            if dest == "N":
                points[0] += 1

            elif dest == "S":
                points[0] -= 1

            elif dest == "E":
                points[1] += 1

            elif dest == "W":
                points[1] -= 1

            if tuple(points) in s:
                return True

        return False
