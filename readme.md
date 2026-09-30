FINGERPRINT SENSOR SYSTEM USING RASPBERRY PI
==============================================

PROJECT OVERVIEW
----------------
This project uses a fingerprint sensor connected to a Raspberry Pi to enroll, search, and delete fingerprints. The program is written in Python and provides a menu-driven interface in the terminal.

The system communicates with the fingerprint sensor through a serial connection. Fingerprint data is converted into templates and stored in the sensor's memory. A user can select an operation from the menu to manage fingerprint records.

OBJECTIVES
----------
- Enroll a new fingerprint.
- Check whether a fingerprint is already registered.
- Delete a stored fingerprint template.
- Understand serial communication between Raspberry Pi and a fingerprint sensor.
- Learn basic Python functions, loops, and exception handling.

HARDWARE REQUIREMENTS
---------------------
- Raspberry Pi
- UART/USB fingerprint sensor module
- USB-to-serial connection (if required by the sensor)
- Jumper wires and power supply, as required by the sensor
- Monitor, keyboard, and mouse for setup

SOFTWARE REQUIREMENTS
---------------------
- Raspberry Pi OS
- Python 3
- Thonny IDE or another Python editor
- pyfingerprint library
- RPi.GPIO library

INSTALLATION
------------
Install the required Python libraries in the Python environment used to run the program. For example:

    python3 -m pip install pyfingerprint RPi.GPIO

Note: Package installation methods can vary depending on the Raspberry Pi OS version. Some systems require a virtual environment or a system package manager.

CONNECTION
----------
Connect the fingerprint sensor to the Raspberry Pi using the connection method supported by your sensor. This program expects the sensor to be available at:

    /dev/ttyUSB0

The serial baud rate configured in the program is:

    57600

The sensor's power, ground, transmit, and receive connections must follow the manufacturer's pinout. Do not assume pin connections without checking the specific sensor model.

HOW TO RUN
----------
1. Connect the fingerprint sensor to the Raspberry Pi.
2. Confirm that the sensor appears at /dev/ttyUSB0.
3. Open Thonny IDE.
4. Copy the Python program into a new file.
5. Save the file as fingerprint_system.py.
6. Run the program.
7. Select an operation from the displayed menu.

MENU OPTIONS
------------
1. Enroll
   Registers a new fingerprint. The user scans the same finger twice so the program can compare the scans and store a template.

2. Search
   Scans a finger and checks whether a matching template exists in the sensor's memory. The program displays the matching template position or reports that no match was found.

3. Delete
   Scans a finger, searches for its stored template, and deletes the template if a match is found.

4. Exit
   Stops the menu loop and ends the program.

WORKING PRINCIPLE
-----------------
1. The program imports the required Python libraries and initializes GPIO settings.
2. It creates a connection to the fingerprint sensor through the configured serial port.
3. The menu allows the user to choose enrollment, search, deletion, or exit.
4. During enrollment, the sensor captures two images of the same finger and compares their characteristics.
5. If the scans match and the fingerprint is not already stored, the program creates and saves a template.
6. During search or deletion, the program captures a fingerprint and compares it with templates stored in the sensor.
7. The program displays the result in the terminal.

TROUBLESHOOTING
---------------
- Sensor not detected: Check the USB/serial connection and confirm the correct device path.
- Permission denied: Check the user's permission to access the serial device.
- Import error: Confirm that the required libraries are installed in the Python environment used by Thonny.
- Fingerprint not recognized: Place the finger correctly on the sensor and try again.
- Enrollment fails: Ensure that both scans are of the same finger and that the sensor surface is clean.
- Incorrect serial settings: Verify the baud rate and communication settings supported by the sensor.

SAFETY AND PRIVACY
------------------
Fingerprint data is biometric information. Use the system only with the consent of the person whose fingerprint is being registered. Protect access to the device and delete stored templates when they are no longer needed.

LIMITATIONS
-----------
- The program depends on the fingerprint sensor model and its supported library.
- The serial device path may differ on another Raspberry Pi.
- The program is a basic educational demonstration and is not intended to serve as a complete security or access-control product.

CONCLUSION
----------
This project demonstrates fingerprint enrollment, identification, and deletion using a Raspberry Pi and Python. It provides practical experience with biometric sensors, serial communication, Python functions, and menu-driven programming.
