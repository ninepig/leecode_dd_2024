class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timedict = dict()


    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message in self.timedict:
            if timestamp - self.timedict[message] < 10:
                return False
            else:
                self.timedict[message] = timestamp
        else:
            self.timedict[message] = timestamp

        return True
