class Time:
    def __init__(self, hours: int = 0, minutes: int = 0):
        self.hours = hours
        self.minutes = minutes
        
    def __str__(self):
        result = str(self.hours)
        if self.minutes < 10:
            result = result + ':0' + str(self.minutes)
        else:
            result = result + ':' + str(self.minutes)
        return result
    
    def add_minutes(self, min_to_add: int):
        self.minutes = self.minutes + min_to_add
        if self.minutes > 60:
            self.hours += self.minutes//60
            self.minutes = self.minutes % 60
        if self.hours >= 24:
            self.hours = self.hours % 24

def main():
    default_time = Time()
    current_time = Time(10, 27)
    later = Time(12, 45)
    current_time.add_minutes(3703)
    print(current_time)
    print(later)
    print(default_time)
    
if __name__ == '__main__':
    main()