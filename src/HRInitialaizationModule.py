import xlrd  # to manipulate excel
import os    # to user loged in user
import time
import HRLettersHandelingModule

# user = os.getlogin()
user = "Fawaz"
giveMeSpaceToMidH = "\t\t\t\t\t  "
giveMeSpaceToMidV = "\n\n\n\n\n"
newLine = "\n"

def Welcome():
    print("\nWelcome " + user +
          ".. \nThis Program was desgnied to help you with your daily tasks " + newLine)

def OpenFile(fileName_):
    global rb
    global fileName 
    
    filePath = ("../resources/" + fileName_ + ".xlsx")    
    try:
        rb = xlrd.open_workbook(filePath)
        sheetDescriptorpar = rb.sheet_by_index(0)
        fileName = fileName_
        SetGlobals(sheetDescriptorpar)
    except OSError as err:
        print("COULD NOT OPEN FILE, " + user + " PLEASE DOUBLE-CHECK FILE NAME \n"
              "NOTE: YOU DO NOT NEED EXTENSION \".xlsx \" " + str(err))
        return -1

def ExtractNumber(message, max):
    while True:
        print(message)
        try:
            userInput = int(input("Please enter a number: "))
            break
        except ValueError:
                print("Oops!  That was no valid number.  Try again...")
    if(userInput >= min and userInput < max+1):        
        return userInput
    else:    
        print("Oops!  The number is out of range.  Try again...")
        userInput = -1 
    return userInput

def Initilaize():
    Welcome()

    global min

    global promptFileOpening
    global fileOpeningMax 
   
    global promptMainCommand
    global mainCommandMax

    min = 0
      
    promptFileOpening = newLine + "Do you want to enter a file name or do you want to use default file?" + newLine + \
        "enter 1. to use default file that was preprogrammed " + newLine + \
        "enter 2. to enter the file name " + newLine + \
        "enter 0. to QUIT the program" + newLine 
    
    fileOpeningMax = 2

    promptMainCommand = "please select what you want to do: " + newLine + \
        "1. View employee's details " + newLine + \
        "2. Generate Letters" + newLine + \
        "3. Vacations Requests " + newLine + \
        "4. View employees salaries within given parameters. Example, salaries less than 15000 and more than 7000" + newLine + \
        "0. to QUIT the program"     
    mainCommandMax = 5

    

def SetGlobals(sheetDescriptorpar):
    global sheetDescriptor
    global parID
    global parName
    global parFullSalary
    global parPosition
    global parMonthsInService
    global parVacationsAvailable
    global parStartDate 
    global parTransportationAllowance
    global parHousingAllowance
    global parBasicSalary
    
    sheetDescriptor = sheetDescriptorpar
    parID = "EmployeeID"
    parName = "Name"
    parFullSalary = "Full Salary"
    parPosition = "Position"
    parMonthsInService = "Service"
    parVacationsAvailable = "Vacations Available"
    parStartDate = "Date Of Start" 
    parTransportationAllowance = "Transportation Allowance"
    parHousingAllowance = "Housing Allowance"
    parBasicSalary = "Basic Salary"

    def SetColumns():
        global employeeIDColLocation  
        global nameColLocation
        global fullSalaryColLocation
        global positionColLocation
        global monthsinServiceColLocation
        global vacationsAvailableColLocation
        global transportationAllowanceColLocation
        global housingAllowanceColLocation
        global basicSalaryColLocation
        global startDateColLocation

        for i in range(sheetDescriptor.ncols): 

            if (sheetDescriptor.cell_value(0, i)) == parID:
                employeeIDColLocation = i
                
            elif (sheetDescriptor.cell_value(0, i)) == parName:
                nameColLocation = i
                
            elif (sheetDescriptor.cell_value(0, i)) == parFullSalary:
                fullSalaryColLocation = i
                
            elif (sheetDescriptor.cell_value(0, i)) == parPosition:
                positionColLocation = i
                
            elif (sheetDescriptor.cell_value(0, i)) == parMonthsInService:
                monthsinServiceColLocation = i
                
            elif (sheetDescriptor.cell_value(0, i)) == parVacationsAvailable :
                vacationsAvailableColLocation = i
                
            elif (sheetDescriptor.cell_value(0, i)) == parStartDate:
                startDateColLocation = i
                
            elif (sheetDescriptor.cell_value(0, i)) == parTransportationAllowance:
                transportationAllowanceColLocation = i
                
            elif (sheetDescriptor.cell_value(0, i)) == parHousingAllowance:
                housingAllowanceColLocation = i
                
            elif (sheetDescriptor.cell_value(0, i)) == parBasicSalary:
                basicSalaryColLocation = i
                
        
#        while(employeeIDColLocation == -1 or nameColLocation == -1 or fullSalaryColLocation == -1 or positionColLocation == -1 \
#            or monthsinServiceColLocation == -1 or vacationsUsedColLocation == -1 or startDateColLocation == -1 or  transportationAllowanceColLocation \
#                or housingAllowanceColLocation == -1 or basicSalaryColLocation == -1): 
#                print ("could not determine one or more columns!!" + newLine + newLine + "it is not safe to continue using the software now, EXITING PROGRAM ...")
#                return

    SetColumns()
                
def HandeleFileOpening ():
    inputNumber = ExtractNumber(promptFileOpening,fileOpeningMax)    
    while(inputNumber == -1):
        inputNumber = ExtractNumber(promptFileOpening,fileOpeningMax)
    if (inputNumber == 1):
        fileName = "HR_testing"
        print("opening Default file ...")
    elif (inputNumber == 2):
        fileName = input("Enter the file name you wish to open: ")            
    sheetDescriptor = OpenFile(fileName) 
    while (sheetDescriptor == -1):
        HandeleFileOpening()
    print("File opened succesfully")
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')
    return

def ExtractIntegers(msg):
    while True:
        try:
            employeeID = int(input(msg))
            #if number1 < 1 or number1 > 10:
            #    raise ValueError #this will send it to the print message and back to the input option
            break
        except:
            print("Please enter a number")

    return employeeID