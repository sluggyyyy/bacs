class Date:
    month_strings = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    
    def __init__(self, month: int = 1, day: int = 1, year: int = 1970):
        self.month = month
        self.day = day
        self.year = year
        
    def __str__(self):
        if self.called_is_valid():
            return f'{self.month}/{self.day}/{self.year}'
        else: return 'Invalid date'
        
    def format_in_words(self) -> str:
        if self.called_is_valid():
            return f'{self.month_strings[self.month - 1]} {self.day}, {self.year}'
        else: return 'Invalid date'
        
    def called_is_valid(self) -> bool:
        if self.month <= 12 and self.month > 0:
            return True
        else: return False

def main():   
    # To properly test your class, do not change the code below
    # three date objects get created by the code below:
    today = Date(1, 27, 2025)
    default_day = Date()
    georgia_birthday = Date(11, 15, 1887)
    # output the three dates in m/d/y format:
    print(today)
    print(default_day)
    print(georgia_birthday)
    # output the three dates using the name of the month:
    print(today.format_in_words())
    print(default_day.format_in_words())
    print(georgia_birthday.format_in_words())
    test_date()

def test_date():
    # Default values, and at least one test for every month, 
    # plus some invalid dates
    test_dates = [((), "1/1/1970", "January 1, 1970"),
                  ((2, 18), "2/18/1970", "February 18, 1970"),
                  ((3, 19, 1911), "3/19/1911", "March 19, 1911"),
                  ((4, 15, 1912), "4/15/1912", "April 15, 1912"),
                  ((5, 5, 1862), "5/5/1862", "May 5, 1862"),
                  ((6, 19, 1865), "6/19/1865", "June 19, 1865"),
                  ((7, 20, 1969), "7/20/1969", "July 20, 1969"),
                  ((8, 6, 1945), "8/6/1945", "August 6, 1945"),
                  ((9, 5, 1882), "9/5/1882", "September 5, 1882"),
                  ((10, 8, 1871), "10/8/1871", "October 8, 1871"),
                  ((11, 9, 1989), "11/9/1989", "November 9, 1989"),
                  ((12, 1, 1955), "12/1/1955", "December 1, 1955"),
                  ((-3, 1, 2025), "Invalid date", "Invalid date"),
                  ((13, 1, 2025),"Invalid date", "Invalid date")]
    for date in test_dates:
        obj = Date(*date[0])
        assert obj.__str__() == date[1], f"Incorrect string representation for (m, d, y) = {date[0]}, you returned {obj.__str__()}"
        assert obj.format_in_words() == date[2], f"Incorrect formatting in words for (m, d, y) = {date[0]}, you returned {obj.format_in_words()}"


if __name__ == "__main__": 
    main()
    test_date()
    print("Your code passed all tests")