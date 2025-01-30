import machine

# Initialize I2C on GPIO 8 (SDA) and GPIO 9 (SCL)
i2c = machine.I2C(0, scl=machine.Pin(21), sda=machine.Pin(20), freq=100000)

# Scan for devices
devices = i2c.scan()

if devices:
    print("✅ I2C devices found:", [hex(dev) for dev in devices])
else:
    print("❌ No I2C devices found. Check wiring!")
