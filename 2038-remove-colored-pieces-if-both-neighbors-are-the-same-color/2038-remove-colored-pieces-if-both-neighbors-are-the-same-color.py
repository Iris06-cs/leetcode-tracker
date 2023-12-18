class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        sub_strs={"AAA":0,"BBB":0}
        for i in range(len(colors)-2):
            sub_str=colors[i:i+3]
            if sub_str=="AAA":
                sub_strs["AAA"]+=1
            
            if sub_str=="BBB":
                sub_strs["BBB"]+=1
        # print(sub_strs)     
        return sub_strs["AAA"]>sub_strs["BBB"]