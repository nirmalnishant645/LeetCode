'''
Write a program to count the number of days between two dates.

The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.

 

Example 1:

Input: date1 = "2019-06-29", date2 = "2019-06-30"
Output: 1
Example 2:

Input: date1 = "2020-01-15", date2 = "2019-12-31"
Output: 15
 

Constraints:

The given dates are valid dates between the years 1971 and 2100.
'''
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        year1 = year2 = month1 = month2 = day1 = day2 = ''
        for i in range(len(date1)):
            if i < 4:
                year1 += date1[i] 
                year2 += date2[i] 
            elif 4 < i < 7:
                month1 += date1[i]
                month2 += date2[i]
            elif 7 < i:
                day1 += date1[i]
                day2 += date2[i]
        year1, year2, month1, month2, day1, day2 = int(year1), int(year2), int(month1), int(month2), int(day1), int(day2)
        
        days1, days2 = self.countDays(day1, month1, year1), self.countDays(day2, month2, year2)
        
        return days2 - days1 if days2 >= days1 else days1 - days2
        
    def countDays(self, day, month, year):
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        count = 0
        
        for i in range(1970, year):
            if (i % 100 and not i % 4) or not i % 400:
                count += 366
            else:
                count += 365
        
        for i in range(month - 1):
            count += months[i]
            
        if ((year % 100 and not year % 4) or not year % 400) and (month > 2 or (month == 2 and day == 29)):
            count += 1
            
        return count + day
