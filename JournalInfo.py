
from __main__ import __name__
class JournalInfo(object):
    
    def __init__(self,rank,groupID,title,category,year,yr1JIF,yr2JIF,yr3JIF,yr4JIF,yr5JIF,fiveYrAvg):
        self.title = title
        self.category = category
        self.year = year
        self.yr1JIF = yr1JIF
        self.yr2JIF = yr2JIF
        self.yr3JIF = yr3JIF
        self.yr4JIF = yr4JIF
        self.yr5JIF = yr5JIF
        self.fiveYrAvg = fiveYrAvg
        self.groupID = groupID
        self.rank = rank
        
    def __str__(self):
        return "%d %s %s %s %d %f %f %f %f %f %f" % (self.rank,self.groupID,self.title,self.category,self.year,self.yr1JIF,self.yr2JIF,self.yr3JIF,self.yr4JIF,self.yr5JIF,self.fiveYrAvg)

    def __repr__(self):
        return self.__str__()
    
    def __lt__(self, other):
        return self.fiveYrAvg>other.fiveYrAvg
    
    #self.title+self.category+self.year+self.yr1JIF+self.yr2JIF+self.yr3JIF+self.yr4JIF+self.yr5JIF+self.year
    
        
        