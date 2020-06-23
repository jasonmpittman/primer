import socket
import netifaces as ni

def createString():

    #Prompt user for the IP of the target honeypot
    target_ip = input("Please enter the ip of the target honeypot: ")

    # Prompt user for interface to use
    interfaces_list = ni.interfaces()
    question_string = "Please choose an interface from this list: "

    # Append the available interfaces to the question
    for interface in interfaces_list:
        question_string += interface
        question_string += " "
    question_string += '\n'

    #Prompt user for question
    interface_choice = input(question_string)

    #Find IP associated with that interface
    interface_ip = ni.ifaddresses(interface_choice)[ni.AF_INET][0]['addr']
    print("The user chose to user interface: ", interface_choice)
    print("That interface uses IP: ", interface_ip)



createString()