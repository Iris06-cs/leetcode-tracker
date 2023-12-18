class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        sub_strs={"AAA":0,"BBB":0}
        for i in range(len(colors)-2):
            if colors[i:i+3]=="AAA":
                sub_strs["AAA"]+=1
            
            if colors[i:i+3]=="BBB":
                sub_strs["BBB"]+=1
  
        return sub_strs["AAA"]>sub_strs["BBB"]