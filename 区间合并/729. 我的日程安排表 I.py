class MyCalendar:
    def __init__(self):
        self.Calendar=[]
    def book(self, startTime: int, endTime: int) -> bool:
        for Time in self.Calendar:
            if Time[0]<startTime<Time[1] or Time[0]<startTime<Time[1] or startTime<Time[0]<endTime:
                return False
        self.Calendar.append([startTime,endTime])
        return True
