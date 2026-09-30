import time
from pyfingerprint.pyfingerprint import PyFingerprint
import RPi.GPIO as gpio


print("Successfully imported fingerprint module")

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)


try:
    f = PyFingerprint(
        '/dev/ttyUSB0',
        57600,
        0xFFFFFFFF,
        0x00000000
    )

except Exception as e:
    print('Exception Message: ' + str(e))


# ================= ENROLL FINGERPRINT =================

def enrollFinger():

    print('Enrolling Finger')
    time.sleep(3)

    print('Place Finger')

    while f.readImage() == False:
        pass

    f.convertImage(0x01)

    result = f.searchTemplate()
    positionNumber = result[0]

    if positionNumber >= 0:
        print('Template already exists at position #' + str(positionNumber))
        time.sleep(2)
        return

    print('Remove finger')
    print('Waiting for same finger')

    time.sleep(3)

    while f.readImage() == False:
        pass

    f.convertImage(0x02)

    if f.compareCharacteristics() == 0:
        print('Fingers do not match')
        time.sleep(2)
        return

    else:
        f.createTemplate()
        positionNumber = f.storeTemplate()

        print('Finger enrolled successfully')
        print('Stored at pos: ' + str(positionNumber))

        time.sleep(2)


# ================= SEARCH FINGERPRINT =================

def searchFinger():

    try:
        print('Waiting for finger...')
        time.sleep(2)

        while f.readImage() == False:
            time.sleep(4)
            return

        f.convertImage(0x01)

        result = f.searchTemplate()
        positionNumber = result[0]

        if positionNumber == -1:
            print('No Match found')
            time.sleep(4)
            return False

        else:
            print('Found template at position ' + str(positionNumber))
            time.sleep(4)
            return True

    except Exception as e:
        print('Operation failed')
        print('Exception message: ' + str(e))
        exit(1)

    return


# ================= DELETE FINGERPRINT =================

def deleteFinger():

    try:
        print('Waiting for finger...')
        time.sleep(2)

        while f.readImage() == False:
            time.sleep(4)
            return

        f.convertImage(0x01)

        result = f.searchTemplate()
        positionNumber = result[0]

        if positionNumber == -1:
            print('No Match found')
            time.sleep(4)
            return False

        else:
            if f.deleteTemplate(positionNumber) == True:
                print('Finger Deleted')

                time.sleep(4)
                return True

    except Exception as e:
        print('Operation failed')
        print('Exception message: ' + str(e))
        exit(1)

    return


# ================= MAIN PROGRAM =================

time.sleep(1)

print('Start')

while True:

    i = int(input(
        "\nEnter:\n"
        "1. Enroll\n"
        "2. Search\n"
        "3. Delete\n"
        "4. Exit\n"
    ))

    if i == 1:
        enrollFinger()

    elif i == 2:
        searchFinger()

    elif i == 3:
        deleteFinger()

    elif i == 4:
        break

    else:
        print("Invalid option!!! Enter Correct")


# ================= PROGRAM ENDS =================