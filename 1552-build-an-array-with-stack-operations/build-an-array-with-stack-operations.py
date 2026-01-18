class Solution:
    def buildArray(self, target, n):
        ops = []
        curr = 1   # stream pointer

        for t in target:
            # push & pop unwanted numbers
            while curr < t:
                ops.append("Push")
                ops.append("Pop")
                curr += 1

            # push the target number
            ops.append("Push")
            curr += 1

        return ops
