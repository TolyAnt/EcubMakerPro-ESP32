# Fantasy Pro II Printer Setup

This project facilitates the setup and connection of a printer using both Wi-Fi and Bluetooth serial communication, implemented on MicroPython-compatible hardware.

## Prerequisites

- A MicroPython-supported device (like ESP32 or ESP8266)
- Access to a Wi-Fi network
- A printer compatible with UART communication
- Basic understanding of MicroPython and electronics

## Installation

1. **Flash MicroPython Firmware**: Ensure your device is running the latest version of MicroPython. You can download the firmware and find flashing instructions at the [official MicroPython website](https://micropython.org/download/).

2. **Upload the Script**: Transfer the main script to your device using a file transfer tool compatible with MicroPython, such as `ampy`, `rshell`, or directly through the REPL.

3. **Hardware Setup**:
    - Connect your printer to the UART pins of your MicroPython device. Ensure the baud rate is set correctly to match your printer's specifications.

## Configuration

1. **Wi-Fi Credentials**: Update the `ssid` and `password` variables in the script with your Wi-Fi network credentials.

2. **Install Required Packages**:
    - Ensure your device is connected to the internet over Wi-Fi.
    - Run the script once to install the `micropython-socket` and `micropython-uos` packages using `upip`.

## Usage

1. **Run the Script**: Execute the script on your device. It will perform the following actions:
    - Connect to the specified Wi-Fi network.
    - Install necessary MicroPython packages.
    - Initialize the Bluetooth serial communication and advertise the device as "Fantasy Pro II".

2. **Connect to Bluetooth**:
    - Use a Bluetooth-enabled device to search for "Fantasy Pro II".
    - Once connected, the script will flash an LED on your MicroPython device three times to indicate a successful connection.

## Troubleshooting

- **Wi-Fi Connection Issues**: Verify your SSID and password. Ensure your MicroPython device is within the range of your Wi-Fi router.
- **Bluetooth Issues**: Ensure your Bluetooth device is compatible and within range. Restart the connection process if needed.
- **LED Does Not Flash**: Check the LED connection and pin number specified in the script.

## Support

For additional support with the setup or operation, refer to the [MicroPython documentation](https://docs.micropython.org/en/latest/) or raise an issue in this repository.

