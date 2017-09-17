class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        func_time = [0 for _ in range(n)]
        call_stack = []
        for each_func_log in logs:
            func_id, status, time = each_func_log.split(":")
            func_id = int(func_id)
            time = int(time)
            if len(call_stack) > 0:
                last_func_id, last_time = call_stack[-1]
            else:
                last_func_id, last_time = -1, 0

            if status == "start":
                if last_func_id >= 0:
                    func_time[last_func_id] += time - last_time
                call_stack.append([func_id, time])
            else:
                call_stack.pop()
                func_time[func_id] += time - last_time + 1
                if len(call_stack) > 0:
                    # We need to set the time of
                    # the top func_id on the stack
                    # to be current time + 1
                    call_stack[-1][1] = time + 1

        return func_time


s = Solution()
logs = ["0:start:0",
 "1:start:2",
 "1:end:5",
 "0:end:6"]
print(s.exclusiveTime(2, logs))
