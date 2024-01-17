class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        # hashmap to track time for each function id {id:[curr_total,start_time]}
        # input logs is array with one function excution info, split each info into array
        # splitted info array[0] will be func id, array[1] status ,array[2] time stamp
        # if status is start, track the start time
        # if status is end, cal curr_total+end-start
        # times={}
        # for log in logs:
        #     splited_log=log.split(":")
        #     print(splited_log)
        #     id=splited_log[0]
        #     status=splited_log[1]
        #     time=splited_log[2]
        #     if id not in times.keys():
        #         times[id]=[0,int(time)]
        #     else:
        #         if status == "start":
        #             times[id][1]=int(time)
        #         if status == "end":
        #             times[id][0]+= (int(time)-times[id][1])
        # print(times)
        # ans=[ info[0] for info in times.values()]
        # return ans
        
        
        stack = []
        prev_time = 0
        ans = [0 for i in range(n)]
        
        for i in range(0,len(logs)):
            fid, state, time = logs[i].split(':')
            fid, time = int(fid), int(time)
            
            if state == "start":
                if stack:
                    ans[stack[-1]] += time - prev_time
                
                stack.append(fid)
                prev_time = time
           
            else:
                ans[stack.pop()] += time - prev_time + 1
                prev_time = time + 1
            
        return ans
        