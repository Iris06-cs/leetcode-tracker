class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
      
        # sort by position, a car further from the destination even with high speed, will not able to pass the car in front of it
        sorted_car = sorted([(position[i],speed[i]) for i in range(len(position)) ],key = lambda x:x[0], reverse = True)
        stack = []
     
        for pos,curr_speed in sorted_car:
            
            time_to_target = (target - pos) / curr_speed
            if not stack or time_to_target > stack[-1]:
                stack.append(time_to_target)
                    
        return len(stack)
        
        