class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not len(intervals):
            return 0
        
        start_time = sorted([interval[0] for interval in intervals])
        end_time = sorted([interval[1] for interval in intervals])
        
        start = end = 0
        rooms = max_rooms = 0
        
        while start < len(intervals):
            if start_time[start] < end_time[end]:
                rooms += 1
                start += 1
            else:
                rooms -= 1
                end +=1
            max_rooms = max(max_rooms,rooms)
        return max_rooms
        