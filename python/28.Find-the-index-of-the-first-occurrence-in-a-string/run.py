#!/usr/bin/python3

import sys
import datetime

from solution import Solution1, Solution2, Solution3

# Class to perform time measurements
class Stopwatch:
    def __init__(self):
        self.start = datetime.datetime.now()

    def stop(self):
        self.stop = datetime.datetime.now()
        self.time = self.stop - self.start

    def print(self, loops = 1):
        step_time = self.time / loops
        print(
            "%sime: %u sec %u usec" %
            ("Loops: %i Time: %u sec %u usec Step t" %
            (loops, self.time.seconds, self.time.microseconds) if loops > 1 else "T",
            step_time.seconds, step_time.microseconds)
        )

# Test solution class
def testSolution(class_name, s1, s2, loops = 1):
    print("Solution: %s" % (class_name))
    solution = class_name()

    time = Stopwatch()

    for l in range(0, loops):
        solution.strStr(s1, s2)

    time.stop()
    time.print(loops)

# Main
if __name__ == "__main__":
    print("Arguments: %s" % (str(sys.argv)))

    if len(sys.argv) != 3:
        print("%s: <s1> <s2>" % (sys.argv[0]))
        sys.exit(0)

    s1 = sys.argv[1]
    s2 = sys.argv[2]

    print("s1: %s S2: %s" % (s1, s2))

    # Test solution:
    loops = 10000

    testSolution(Solution1, s1, s2, loops)
    testSolution(Solution2, s1, s2, loops)
    testSolution(Solution3, s1, s2, loops)
