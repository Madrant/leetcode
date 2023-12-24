class Solution:
    def isPathCrossing(self, path: str) -> bool:

        path = list(path)

        d = {
            "N": [0, +1],
            "S": [0, -1],
            "E": [+1, 0],
            "W": [-1, 0]
        }

        # A dict to count visited coordinates
        count = {}

        # Start from center
        coord = [0, 0]
        count[tuple(coord)] = 1

        while len(path):
            c = path.pop()
            p = d[c]

            # Move to the direction
            coord[0] += p[0]
            coord[1] += p[1]

            # Count visited coordinates
            if tuple(coord) in count:
                count[tuple(coord)] += 1
            else:
                count[tuple(coord)] = 1

            # Check if there is a point visited twice
            if count[tuple(coord)] >= 2:
                return True

        return False
