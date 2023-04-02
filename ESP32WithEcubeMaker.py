import bluetooth
import machine
import time

# Set up the serial connection to the printer
uart = machine.UART(1, baudrate=115200)
uos.dupterm(uart, 1)

# Connect to your Wi-Fi network
ssid = "your_wifi_ssid"
password = "your_wifi_password"
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect(ssid, password)
while not sta_if.isconnected():
    pass

# Install the required packages
upip.install('micropython-socket')
upip.install('micropython-uos')

# Set up Bluetooth serial
bluetoothSerial = bluetooth.BluetoothSerial()
bluetoothSerial.init()
bluetoothSerial.advertise("Fantasy Pro II")

# Loop to wait for Bluetooth connection
while True:
    if bluetoothSerial.connected():
        print("Connected")
        # Flash the LED 3 times to indicate successful connection
        for i in range(3):
            machine.Pin(2, machine.Pin.OUT).on()
            time.sleep(0.5)
            machine.Pin(2, machine.Pin.OUT).off()
            time.sleep(0.5)
        break
    else:
        print("Waiting for connection")
        time.sleep(1)
