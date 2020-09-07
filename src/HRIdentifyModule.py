import HRInitialaizationModule
import os    #to user loged in user

def IdentifyEmployee(employeeName): 
    sheetDescriptor = HRInitialaizationModule.sheetDescriptor
#    wb = copy(HRInitialaizationModule.rb)
#    w_sheet = wb.get_sheet(0)
    employeeRowLocation = -1
    for i in range(sheetDescriptor.nrows):
        if (sheetDescriptor.cell_value(i, HRInitialaizationModule.nameColLocation)) == employeeName:
            employeeRowLocation = i
            print("FOUND EMPLOYEE, value is " + str(employeeRowLocation))
    if (employeeRowLocation == -1):    
        print ("Could not find employee")
        return employeeRowLocation
    convertedID = str(sheetDescriptor.cell_value(
        employeeRowLocation, HRInitialaizationModule.employeeIDColLocation))
    convertedName = str(sheetDescriptor.cell_value(
        employeeRowLocation, HRInitialaizationModule.nameColLocation))
    convertedPosition = str(sheetDescriptor.cell_value(
        employeeRowLocation, HRInitialaizationModule.positionColLocation))
    convertedMonthsInService = str(int(sheetDescriptor.cell_value(
        employeeRowLocation, HRInitialaizationModule.monthsinServiceColLocation)))
    convertedVacationsAvailable = str(int(sheetDescriptor.cell_value(
        employeeRowLocation, HRInitialaizationModule.vacationsAvailableColLocation)))

    confirmEmployee = input("please confirm that employee you are looking for is " + convertedName + "? \n (please type Yes or No)")
    if (confirmEmployee == "yes" or confirmEmployee == "Yes" or confirmEmployee == "YES"):
        employeeInfo = "you are retrieving the information of: " + convertedName + HRInitialaizationModule.newLine + \
        "ID: " + convertedID + HRInitialaizationModule.newLine + \
        "Position: " + convertedPosition + HRInitialaizationModule.newLine + \
        "Vacations Available:" + convertedVacationsAvailable + HRInitialaizationModule.newLine + \
        "Months in service: " + convertedMonthsInService + HRInitialaizationModule.newLine

        print(employeeInfo)
        input("When you are ready, Please Press Enter to continue...")
        return
    
    return -1