class Date:
    month_strings = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    days_non_leap = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    def __init__(self, month: int = 1, day: int = 1, year: int = 1970):
        self.month = month
        self.day = day
        self.year = year
        
    def __lt__(self, other):
        if self.year < other.year: return True
        elif self.year > other.year: return False
        elif self.month < other.month: return True
        elif self.month > other.month: return False
        elif self.day < other.day: return True
        elif self.day > other.day: return False
        
        
    def __eq__(self, other) -> bool:
        return self.month == other.month and self.day == other.day and self.year == other.year
        
    def __str__(self):
        if self.is_valid():
            return f'{self.month}/{self.day}/{self.year}'
        else: return 'Invalid date'
        
    def format_in_words(self) -> str:
        if self.is_valid():
            return f'{self.month_strings[self.month - 1]} {self.day}, {self.year}'
        else: return 'Invalid date'
        
    def is_valid(self) -> bool:
        if self.month > 12 or self.month < 1 :
            return False
        days_in_month = Date.days_leap if self.is_leap_year() else Date.days_non_leap
        if self.day < 1 or self.day > int(days_in_month[self.month - 1]):
            return False
        return True
        
    def is_leap_year(self) -> bool:
        if (self.year % 4 == 0 and self.year % 100 != 0 and self.year > 1582) or (self.year % 400 == 0 and self.year > 1582):
            return True
        else: return False
        
    def advance(self):
        days_in_month = Date.days_leap if self.is_leap_year() else Date.days_non_leap
        
        self.day += 1
        if self.day > days_in_month[self.month - 1]:
            self.day = 1
            self.month += 1
            if self.month > 12:
                self.month = 1
                self.year += 1
                
    def day_of_year(self) -> int:
        days_in_month = Date.days_leap if self.is_leap_year() else Date.days_non_leap
        return sum(days_in_month[:self.month - 1]) + self.day
            
            

date1 = Date(11, 4, 2007)
print(date1)
date2 = Date(11, 4, 2007)
print(date2)
date3 = date2

print(id(date1))
print(id(date2))

print(date1 is date2)

print(date1== date2)

date4 = Date(12, 4, 1995)
date5 = Date(12, 30, 1995)
print(date4 < date5)