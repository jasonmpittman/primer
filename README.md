# primer
Primer is a honeypot research tool which uses automated attacks, in the form of Packet Capture(PCAP) files to generate identical activity and logs.

# USE
To use primer, navigate into the `bin` directory and run the command `sudo python3 primer.py`
This command will open the Graphical User Interface(GUI).
The GUI is seperated into sections. The main section is where the user will select the PCAPs that they want to run, sorted by the services that these pcaps test.
The user will then input the IP Address of the Honeypot that they want to test against.
Lastly, the user indicates which network interface they want to utilize when sending the command.
Hitting the RUN button will launch the PCAP against the designated Honeypot.
The program will return a dialog window detailing whether the PCAP successfully or unsuccesfully ran, indicating a log file in which the user can navigate to to see the results of the PCAP.


## Adding a PCAP
The `Add PCAP` section of the GUI allows for a user to select a PCAP file from their local directories, upload it to primer, and allow for the program to use it as a testing tool.
To add a pcap, the user must select the PCAP file using the file chooser browser that appears when the `Add File` button is pressed.
The user will then specify which services the PCAP will test against, allowing the uploaded PCAP to be sorted appropriately into the services on the left-hand side of the screen.
The user must also specify the IP of the Source and Destination machines in which the desired PCAP ran against. This allows Primer to automatically run the PCAP.
Once the `Add PCAP` button is selected, a dialog box will appear detailing if the PCAP was successfully added.
In order to view the newly added PCAP the user must restart the primer tool.

## Dependencies
The user must install some python dependencies in order for primer to work effectively.
These dependencies include:
```
tkinter
tcpreplay-edit
```
For Ubuntu-based systems, one may install these dependencies by running the command: 
```
sudo apt install -y python3-tk tcpreplay
```

## Note: Primer will not work using the Windows Linux Subsystem
The primer tool must be run on a dedicated linux machine or linux virtual environment.
Due to the nature of the WSL, primer cannot access network interfaces through the WSL and therefore cannot run the primer tool.
