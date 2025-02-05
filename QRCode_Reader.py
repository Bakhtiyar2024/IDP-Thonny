import struct
from time import sleep
import machine

class QRCodeReader:
    def __init__(self, i2c_id=1, scl_pin=17, sda_pin=16, freq=100000, address=0x0C, delay=0.1):
        """
        Initializes the QR Code Reader on I2C.

        :param i2c_id: I2C bus number (1 for Pico W default)
        :param scl_pin: GPIO pin number for SCL
        :param sda_pin: GPIO pin number for SDA
        :param freq: I2C clock speed (default 100kHz for stability)
        :param address: I2C address of the QR code reader
        :param delay: Delay between each read cycle
        """
        self.address = address
        self.delay = delay

        # Message format constants
        self.length_offset = 0
        self.length_format = "H"
        self.message_offset = struct.calcsize(self.length_format)
        self.message_size = 254
        self.message_format = "B" * self.message_size
        self.i2c_format = self.length_format + self.message_format
        self.i2c_byte_count = struct.calcsize(self.i2c_format)

        # Initialize I2C
        self.i2c = machine.I2C(i2c_id, scl=machine.Pin(scl_pin), sda=machine.Pin(sda_pin), freq=freq)

        # Check if the QR reader is detected
        self._check_device()

    def _check_device(self):
        """ Scans for I2C devices and ensures the QR reader is connected. """
        devices = self.i2c.scan()
        print("I2C devices found:", [hex(dev) for dev in devices])
        
        if self.address not in devices:
            raise Exception("Error: QR Code Reader NOT detected! Check wiring.")

    def read_qr_code(self):
        """
        Reads and decodes the QR code from the sensor.
        
        :return: Decoded QR code string, or None if no QR code is detected.
        """
        sleep(self.delay)

        try:
            # Read data from the sensor
            read_data = self.i2c.readfrom(self.address, self.i2c_byte_count)

            # Extract message length from the first two bytes
            message_length, = struct.unpack_from(self.length_format, read_data, self.length_offset)

            if message_length == 0:
                return None  # No QR code detected

            # Extract and decode message bytes
            message_bytes = read_data[self.message_offset:self.message_offset + message_length]
            return message_bytes.decode("utf-8")

        except UnicodeDecodeError:
            print("Error: Unable to decode message. Check if it’s valid UTF-8.")
            return None
        except OSError as e:
            print("I2C Read Error:", e)
            return None
        

def main():
    try:
        qr_reader = QRCodeReader()  # Initialize the QR code reader
        print("QR Code Reader initialized successfully.")

        while True:
            qr_code = qr_reader.read_qr_code()
            if qr_code:
                print(f"QR Code Detected: {qr_code}")
            else:
                print("No QR Code detected.")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()

