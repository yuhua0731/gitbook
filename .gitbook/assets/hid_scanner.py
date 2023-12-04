import hid
import time

class HIDScanner:
    _character_dict = {
        0x04: ["a", "A"],
        0x05: ["b", "B"],
        0x06: ["c", "C"],
        0x07: ["d", "D"],
        0x08: ["e", "E"],
        0x09: ["f", "F"],
        0x0a: ["g", "G"],
        0x0b: ["h", "H"],
        0x0c: ["i", "I"],
        0x0d: ["j", "J"],
        0x0e: ["k", "K"],
        0x0f: ["l", "L"],
        0x10: ["m", "M"],
        0x11: ["n", "N"],
        0x12: ["o", "O"],
        0x13: ["p", "P"],
        0x14: ["q", "Q"],
        0x15: ["r", "R"],
        0x16: ["s", "S"],
        0x17: ["t", "T"],
        0x18: ["u", "U"],
        0x19: ["v", "V"],
        0x1a: ["w", "W"],
        0x1b: ["x", "X"],
        0x1c: ["y", "Y"],
        0x1d: ["z", "Z"],
        0x1e: ["1", "!"],
        0x1f: ["2", "@"],
        0x20: ["3", "#"],
        0x21: ["4", "$"],
        0x22: ["5", "%"],
        0x23: ["6", "^"],
        0x24: ["7", "&"],
        0x25: ["8", "*"],
        0x26: ["9", "("],
        0x27: ["0", ")"],
        0x2d: ["-", "_"],
        0x2e: ["=", "+"],
        0x2f: ["[", "{"],
        0x30: ["]", "}"],
        0x31: ["\\", "|"],
        0x33: [";", ":"],
        0x34: ["'", "\""],
        0x35: ["`", "~"],
        0x36: [",", "<"],
        0x37: [".", ">"],
        0x38: ["/", "?"]
    }

    
    def __init__(self):
        self.hid_device = hid.device()
        return
    
    def __del__(self):
        self.hid_device.close()
        return

    def scan(self, vendor_id, product_id):        
        device_dict = dict()
        devices = hid.enumerate(vendor_id, product_id)

        if len(devices) == 0:
            raise Exception("No SM-2D device found")
        elif len(devices) > 1:
            print("Multiple SM-2D devices found, please select a device:")
            for i in range(len(devices)):
                print(f"{i}: {devices[i]['product_string']}")
            while True:
                try:
                    index = int(input("Enter the index of the device you want to use: "))
                    if index < 0 or index >= len(devices):
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid index, please try again.")
            
            device_dict = devices[index]
        else:
            device_dict = devices[0]

        self.hid_device.open(device_dict['vendor_id'], device_dict['product_id'], device_dict['serial_number'])
        print("Manufacturer: %s" % self.hid_device.get_manufacturer_string())
        print("Product: %s" % self.hid_device.get_product_string())
        print("Serial No: %s" % self.hid_device.get_serial_number_string())

    def _shift_pressed(self, caps_lock, shift):
        result = False
        if (caps_lock and not shift) or (not caps_lock and shift):
            result = True
        return result

    def _hid_keyboard_decode(self, line, result):
        caps_lock = False
        modifier = line[0]
        if modifier == 0x20 or modifier == 0x02:
            shift = True
        else:
            shift = False

        key = line[2]
        if key != 0:
            if key == 0x39:
                caps_lock = not caps_lock
            elif key == 0x56:
                print("-")
                result.append("-")
            elif 0x04 <= key <= 0x1d:
                if self._shift_pressed(caps_lock, shift):
                    result.append(self._character_dict[key][1])
                else:
                    result.append(self._character_dict[key][0])
            else:
                if shift:
                    result.append(self._character_dict[key][1])
                else:
                    result.append(self._character_dict[key][0])

    def read(self, maxLen, data, timeout):
        end_time = int(round(time.time() * 1000)) + timeout
        remaining_time = timeout

        while True:
            ret = self.hid_device.read(8, 200)
            remaining_time = end_time - int(round(time.time() * 1000))

            if ret:
                self._hid_keyboard_decode(ret, data)
            
            # If the data length is greater than the maximum length, or the data length is 0, break out of the loop.
            if (len(data) >= maxLen) or (len(ret) == 0):
                break

            # If the remaining time is less than 0 and the data length is 0, break out of the loop.
            if (remaining_time <= 0) and (len(ret) == 0):
                break
        return

