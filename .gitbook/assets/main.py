import signal
from hid_scanner import HIDScanner

global_continue_reading = True
# Capture SIGINT for cleanup when the script is aborted
def end_read(signal, frame):
    global global_continue_reading
    print("Ctrl+C captured, ending read.")
    global_continue_reading = False

try:
    # Hook the SIGINT
    signal.signal(signal.SIGINT, end_read)
    scanner = HIDScanner()
    scanner.scan(0xac90, 0x3002)

    # read back the answer
    print("Read the data")
    decode_result = []
    while global_continue_reading:
        scanner.read(128, decode_result, 2000)
        if decode_result:
            print("len:", len(decode_result))
            print("".join(decode_result))
            decode_result = []

except IOError as ex:
    print(ex)
    print("You probably don't have the hard-coded device.")
    print("Update the h.open() line in this script with the one")
    print("from the enumeration list output above and try again.")