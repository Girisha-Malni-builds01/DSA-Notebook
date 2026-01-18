class Solution:
    def exclusiveTime(self, n, logs):
        res = [0] * n
        stack = []          # holds function IDs
        prev_time = 0       # last processed timestamp

        for log in logs:
            fid, typ, ts = log.split(':')
            fid, ts = int(fid), int(ts)

            if typ == "start":
                # Give time to the previously running function
                if stack:
                    res[stack[-1]] += ts - prev_time
                stack.append(fid)
                prev_time = ts

            else:  # "end"
                # End current function and compute its duration
                res[stack.pop()] += ts - prev_time + 1
                prev_time = ts + 1   # next time unit starts after this end

        return res
