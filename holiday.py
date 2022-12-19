import datetime
import json
from bs4 import BeautifulSoup
import requests
from dataclasses import dataclass


# -------------------------------------------
# Modify the holiday class to 
# 1. Only accept Datetime objects for date.
# 2. You may need to add additional functions
# 3. You may drop the init if you are using @dataclasses
# --------------------------------------------
@dataclass
class Holiday:
    name: str
    date: datetime.date
    
    def __str__ (self):
        return f'{self.name} ({self.date})'

    
           
# -------------------------------------------
# The HolidayList class acts as a wrapper and container
# For the list of holidays
# Each method has pseudo-code instructions
# --------------------------------------------
class HolidayList:
    def __init__(self):
       self.innerHolidays = []
   
    def addHoliday(self, holidayObj):
        # Make sure holidayObj is an Holiday Object by checking the type
        if not isinstance(holidayObj, Holiday):
            raise TypeError("Incorrect data type.")
        
        # Use innerHolidays.append(holidayObj) to add holiday
        self.innerHolidays.append(holidayObj)
        # print to the user that you added a holiday
        print(f"Adding {self.innerHolidays[-1]} to the Holiday list.")

    def findHoliday(self, name, date):
        # Find Holiday in innerHolidays
        findHoliday = Holiday(name, date)
        
        for i in self.innerHoliday:
            if findHoliday == i:
                return i
        return False
        # Return Holiday

    def removeHoliday(name, date):
        # Find Holiday in innerHolidays by searching the name and date combination.
        removeHoliday = self.findHoliday(name, date)
        
        if removeHoliday == False:
            return False
        else:
        # remove the Holiday from innerHolidays
            self.innerHolidays.remove(removeHoliday)
        # inform user you deleted the holiday
            print('Holiday removed.')

    def read_json(self, filelocation):
        # Read in things from json file location
        with open (filelocation) as f:
            data = json.load(f)
            for i in data['holidays']:
                holiday = i['name']
                date = i['date']
                date = date.split('-')
                date = datetime.date(int(date[0]), int(date[1]), int(date[2]))
                self.addHoliday(Holiday(holiday, date))
            f.close()
        # Use addHoliday function to add holidays to inner list.
        pass

    def save_to_json(self, filelocation):
        # Write out json file to selected file.
        with open(filelocation, 'w') as f:
            for i in self.innerHolidays:
                json.dump({'name': i.name, 'date': str(i.date)}, f, indent = 4)
        
    def scrapeHolidays():
        # Scrape Holidays from https://www.timeanddate.com/holidays/us/ 
        # Remember, 2 previous years, current year, and 2  years into the future. You can scrape multiple years by adding year to the timeanddate URL. For example https://www.timeanddate.com/holidays/us/2022
        # Check to see if name and date of holiday is in innerHolidays array
        # Add non-duplicates to innerHolidays
        # Handle any exceptions.     
        pass

    def numHolidays(self):
        return len(self.innerHolidays)
    
    def filter_holidays_by_week(year, week_number):
        # Use a Lambda function to filter by week number and save this as holidays, use the filter on innerHolidays
        # Week number is part of the the Datetime object
        # Cast filter results as list
        # return your holidays
        pass

    def displayHolidaysInWeek(holidayList):
        # Use your filter_holidays_by_week to get list of holidays within a week as a parameter
        # Output formated holidays in the week. 
        # * Remember to use the holiday __str__ method.
        pass

    def getWeather(weekNum):
        # Convert weekNum to range between two days
        # Use Try / Except to catch problems
        # Query API for weather in that week range
        # Format weather information and return weather string.
        pass

    def viewCurrentWeek():
        # Use the Datetime Module to look up current week and year
        # Use your filter_holidays_by_week function to get the list of holidays 
        # for the current week/year
        # Use your displayHolidaysInWeek function to display the holidays in the week
        # Ask user if they want to get the weather
        # If yes, use your getWeather function and display results
        pass

url = "https://www.timeanddate.com/holidays/us/"
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

type(res.text)

table = soup.find_all('table')[0]
trs = table.find_all('tr')
info = trs[1]
info1 = trs[3]
name = info1.find_all('a')[0]
name_alone = name.attrs['href']
info2 = info1.find("th")


# string = '2021-02-17'
# string = string.split('-')
# date = datetime.date(int(string[0]), int(string[1]), int(string[2]))

# print(date)

# date.isocalendar()[1]


# helper function

def helper1(holidayList):
    print('Add a Holiday')
    name = input('Enter a Holiday: ')
    date = input('Enter a date (yyyy-mm-dd): ')
    date = date.split("-")
    while type(date) != datetime.date:
        try: 
            date = datetime.date(int(date[0]), int(date[1]), int(date[2]))
        except:
            print("Invalid...Try again.")
            date = input('Enter a date (yyyy-mm-dd): ')
            date = date.split("-")
            
    holidayObj = Holiday(name, date)
    holidayList.addHoliday(holidayObj)
    print("Holiday has been added")
    
def helper2(holidayList):
    print('Remove a Holiday')
    name = input('Please enter the name of the Holiday you would like to remove: ')
    date = input('Enter a date (yyyy-mm-dd): ')
    date = date.split("-")
    while type(date) != datetime.date:
        try: 
            date = datetime.date(int(date[0]), int(date[1]), int(date[2]))
        except:
            print("Invalid...Try again.")
            date = input('Enter a date (yyyy-mm-dd): ')
            date = date.split("-")
    holidayObj = Holiday(name, date)
    holidayList.removeHoliday(holidayObj)
    print("Holiday has been removed")
    
        
            
def helper3(holidayList):
    print('Saving Holiday List')
    save = input('Do you want to save(y/n): ')
    if save == 'y':
        filename = 'output.json'
        holidayList.save_to_json(filename)
    elif save == 'n':
        print('Holiday list file save canceled.')
    else:
        print('Please enter (y/n): ')
        helper3(holidayList)
        
def helper4(holidayList):
    print('View a Holiday')
    view = input('Please enter the Holiday you would like to view.')
    if view in holidayList:
        print(view)
        holidayList.displayHolidaysInWeek()
    else:
        print("Whoops! That Holiday is not in our system!")
        helper2(holidayList)

def main():
    # Large Pseudo Code steps
    # -------------------------------------
    # 1. Initialize HolidayList Object
    holidayList = HolidayList()
    # 2. Load JSON file via HolidayList read_json function
    # fileLocation = 'holiday.json'
    # holidayList.read_json(fileLocation)
    # 3. Scrape additional holidays using your HolidayList scrapeHolidays function.
    
    holidayList.read_json('holidays.json')
    print("Holiday Management \n==================")
    print(f'There are {holidayList.numHolidays()} holidays stored in the system.')
    # 3. Create while loop for user to keep adding or working with the Calender
    stillinMenu = True
    while stillinMenu:
    # 4. Display User Menu (Print the menu)
        print("Holiday Menu \n============")
        holiday_menu = ['Add a Holiday', 'Remove a Holiday', 'Save Holiday List', 'View Holiday', 'Exit']
        for i in range(len(holiday_menu)):
            print(f'{i + 1}. {holiday_menu[i]}')
    # 5. Take user input for their action based on Menu and check the user input for errors
        menu_choice = int(input("Please enter a menu option number: "))
    # 6. Run appropriate method from the HolidayList object depending on what the user input is
        if menu_choice == 1:
            helper1(holidayList)
        elif menu_choice == 2:
            holidayList.removeHoliday()
        elif menu_choice == 3:
            helper3(holidayList)
        elif menu_choice == 4:
            helper4(holidayList)
        elif menu_choice == 5:
            print("Have a nice day!")
            stillinMenu = False
        else:
            continue
    # 7. Ask the User if they would like to Continue, if not, end the while loop, ending the program.  If they do wish to continue, keep the program going. 


if __name__ == "__main__":
    main();


# Additional Hints:
# ---------------------------------------------
# You may need additional helper functions both in and out of the classes, add functions as you need to.
#
# No one function should be more then 50 lines of code, if you need more then 50 lines of code
# excluding comments, break the function into multiple functions.
#
# You can store your raw menu text, and other blocks of texts as raw text files 
# and use placeholder values with the format option.
# Example:
# In the file test.txt is "My name is {fname}, I'm {age}"
# Then you later can read the file into a string "filetxt"
# and substitute the placeholders 
# for example: filetxt.format(fname = "John", age = 36)
# This will make your code far more readable, by seperating text from code.





