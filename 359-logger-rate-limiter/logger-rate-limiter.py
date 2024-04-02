class Logger:

    def __init__(self):
        self.msgs = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.msgs:
            # add next allowed timestamp as value
            self.msgs[message] = timestamp
            return True
        else:
            if timestamp - self.msgs[message] >= 10:
                # update timestamp in logger, return true
                self.msgs[message] = timestamp
                return True
            else:
                return False
            
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)