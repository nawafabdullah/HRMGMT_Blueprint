import HRInitialaizationModule
import HRLettersHandelingModule
import HRVacationsModule
import HRIdentifyModule
import os
import time

# def TemporaryClean():
#    del convertedID
#    del convertedName
#    del splitNameString
#    del convertedSalary
#    del convertedPosition
#    del convertedMonthsInService


def main():
    while True:
        userInput = HRInitialaizationModule.ExtractNumber(
            HRInitialaizationModule.promptMainCommand, HRInitialaizationModule.mainCommandMax)
        while (userInput == -1):
            userInput = HRInitialaizationModule.ExtractNumber(
                HRInitialaizationModule.promptMainCommand, HRInitialaizationModule.mainCommandMax)
        if (userInput == 1):
            retrieveRequest = HRIdentifyModule.IdentifyEmployee(
                input("enter an employee Name "))
            while (retrieveRequest == -1):
                retrieveRequest = HRIdentifyModule.IdentifyEmployee(
                    input("enter an employee Name "))
        elif (userInput == 2):
            letterRequest_generation = HRLettersHandelingModule.GenerateEmployeeLetters(
                #int(input("enter an employee ID ")))
                HRInitialaizationModule.ExtractIntegers("enter an employee ID "))
            while (letterRequest_generation == -1):
                letterRequest_generation = HRLettersHandelingModule.GenerateEmployeeLetters(
                    HRInitialaizationModule.ExtractIntegers("enter an employee ID "))
        elif (userInput == 3):
            vactionRequest_status = HRVacationsModule.processVacationRequest(HRInitialaizationModule.ExtractIntegers("enter an employee ID "),
                                                                            HRInitialaizationModule.ExtractIntegers("enter the number of days of the vacation"))
            while (vactionRequest_status == -1):
                vactionRequest_status = HRVacationsModule.processVacationRequest(int(input("enter an employee ID ")),
                                                                                (int(input("enter the number of days of the vacation "))))

        elif (userInput == 4):
            print("Not implemented yet")

        elif (userInput == 0):
            print("Thank you for using the program.." +
                  HRInitialaizationModule.newLine + "Have a nice day..")
            break

        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')

#    input(commandInput)
    # if (commandInput == )
HRInitialaizationModule.Initilaize()
HRInitialaizationModule.HandeleFileOpening()
main()
