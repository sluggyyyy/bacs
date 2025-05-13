# class Worker:

#     # initialization method
#     def __init__(self, name: str, wage: float, hours: float):
#         self.name = name
#         self.wage = wage
#         self.hours = hours

#     # reduce a string representation of this worker's information
#     def __str__(self)->str:
#         return f"{self.name}: ${self.wage} hourly wage, {self.hours} hours worked."

#     # print a paycheck to worker resetting hours worked
#     def issue_paycheck(self):
#         print(f"Printing paycheck for ${self.unpaid_wages()} written to {self.name}")
#         self.hours = 0

#     # return amount owed to worker, rounded to nearest penny
#     def unpaid_wages(self)->float:
#         if self.hours <= 40:
#             return round(self.wage*self.hours, 2)
#         else:
#             return round(self.wage*40 + 1.5*self.wage*(self.hours-40), 2)

#     # increase/decrease wage (error check that new wage isn't negative)
#     def change_wage(self, change):
#         if change < 0 and self.wage+change < 0:
#             raise ValueError(f"Worker: wage cannot become negative for {self.name}.")
#         self.wage += change

#     # Increment the number of hours worked (not allowed to decrement hours)
#     def add_hours(self, hours):
#         if hours < 0:
#             raise ValueError(f"Worker: {self.name} annot work negative hours.")
#         self.hours += hours

# def main():
#     # instantiate an object named worker1, initializing name to "Raja Hansen", wage to 15.25, and hours worked to 45
#     worker1 = Worker("Raja Hansen", 15.25, 45)
#     # instantiate an object named worker2, initializing name to "Elian Reyes", wage to 20.50, and hours worked to 40
#     worker2 = Worker("Elian Reyes", 20.50, 40)
#     # instantiate an object named worker3, initializing name to "Cameron Scott", wage to 24.75, and hours worked to 25.5
#     worker3 = Worker("Cameron Scott", 24.75, 25.5)
#     # output the contents of each of the three objects, using the Worker class's __str__ method.
#     print(worker1)
#     print(worker2)
#     print(worker3)
#     # output the pay owed for each worker (invoking the appropriate method from the Worker class)
#     print(worker1.unpaid_wages())
#     print(worker2.unpaid_wages())
#     print(worker3.unpaid_wages())
#     # issue a paycheck for worker1 (invoking the appropriate method from the Worker class)
#     worker1.issue_paycheck()
#     # output the pay now owed to worker1
#     print(worker1.unpaid_wages())
#     # give worker2 a $1.50/hour raise
#     worker2.change_wage(1.50)
#     # increase worker3's hours worked by 15,
#     worker3.add_hours(15)
#     # and reduce worker3's wage by $0.50
#     worker3.change_wage(-0.50)
#     # output the pay owed to worker1, worker2 and worker3
#     print(worker1.unpaid_wages())
#     print(worker2.unpaid_wages())
#     print(worker3.unpaid_wages())

# if __name__ == "__main__":
#     main()

# # If we follow the typical way objects are created in python,
# # the following line instantiates a str object:
# message = str("\tHooray for classes/objects!\n\t    (in python)    ")
# # However, str objects are so common, python allows you to
# # instantiate a str with this shorthand:
# message = "\tHooray for classes/objects!\n\t    (in python)    "

# # output message:
# print(message)

# # output the index of the first 't' in message:
# print(message.index('t'))

# # output the index of the second 't' in the message:
# print(message.index('t', 26))

# # Create a list of str objects, stored in a variable called split_message,
# # one string for each line in message.
# # Each element in the list should not include the "\n" at the end
# split_message = message.splitlines()
# print(split_message)

# # Remove all the whitespace at the *beginning* of each string in split_message
# new_lines = [i.strip() for i in split_message]
# print(new_lines)

# # Output the updated variable split_message

# class ClockTime12:

#     # initialization function, called when object is instantiated
#     def __init__(self, hour: int = 12, minute: int = 0, second: int=0):
#         # initialize the three instance variables.
#         # Note that the default time is 12:00:00
#         self.hour = hour
#         self.minute = minute
#         self.second = second
#         # Check each variable, reset value to default if invalid
#         if hour <= 0 or hour > 12:
#             self.hour = 12
#         if self.minute < 0 or self.minute > 59:
#             self.minute = 0
#         if self.second <= 0 or self.second > 59:
#             self.second = 0
    
#     # return a string representation of the clock time
#     # in the form hh:mm:ss
#     def __str__(self)->str:
#         result = str(self.second)
#         if self.second < 10:
#             result = "0" + result
#         result = str(self.minute) + ":" + result
#         if self.minute < 10:
#             result = "0" + result
#         result = str(self.hour) + ":" + result
#         return result
    
#     # advance the time by add_seconds seconds
#     def advance_seconds(self, add_seconds=1):
#         self.second += add_seconds
#         if self.second > 59:
#             # increase minutes by the number of whole minutes
#             self.minute += self.second//60
#             self.second = self.second%60
#             if self.minute > 59:
#                 # increase hours by the number of whole hours
#                 self.hour += self.minute//60
#                 self.minute = self.minute%60
#                 # If we've gone over 12 hours, subtract multiples of 12
#                 if self.hour > 12:
#                     self.hour = self.hour % 12
#                     # There's no 0 on a 12-hour clock
#                     if self.hour == 0:
#                         self.hour = 12
                

# def main():
#     # instantiate a ClockTime12 object, with the default time  
#     clock = ClockTime12()
#     # create a ClockTime12 object called late_night, to represent 11:59
#     late_night = ClockTime12(hour= 11, minute = 59)
#     # instantiate an invalid ClockTime12 object called wrong
#     # with h = 36, m = 61, s = -1
#     wrong = ClockTime12(hour= 36, minute= 61, second= -1)
#     # instantiate a ClockTime12 object called breakfast, to represent 8:20:30
#     breakfast = ClockTime12(hour = 8, minute = 20, second = 30 )
#     # output the contents of all four objects to the terminal
#     print(clock, late_night, wrong, breakfast)
#     # add one second to the default time, then output its new value

#     # add 3661 seconds to late_night (one hour and 61 seconds), then output

#     # add 43231 seconds to breakfast

#     # output the contents of all four objects


# if __name__ == "__main__":
#     main()