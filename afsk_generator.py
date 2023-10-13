import machine
import utime
import math
import socket

# Constants
BAUD_RATE = 1200
TONE_1_FREQ = 1200  # Tone 1 frequency in Hz
TONE_2_FREQ = 2200  # Tone 2 frequency in Hz
OUTPUT_PIN = 25  # Output pin on ESP32

# Initialize the output pin
output_pin = machine.Pin(OUTPUT_PIN, machine.Pin.OUT)

# Create a socket server for receiving serial data over Wi-Fi
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 9600))  # Listening on port 9600
server_socket.listen(1)

# Wait for a connection
print("Waiting for a connection...")
client_socket, client_address = server_socket.accept()
print(f"Connected to {client_address}")

# Function to generate AFSK signal
def afsk(signal):
    for byte in signal:
        for bit in range(8):
            if (byte >> bit) & 1:
                for i in range(BAUD_RATE):
                    output_pin.value(1)  # Set tone 1
                    utime.sleep_us(int(1e6 / (TONE_1_FREQ * 2)))
                    output_pin.value(0)  # Clear tone 1
                    utime.sleep_us(int(1e6 / (TONE_1_FREQ * 2)))
            else:
                for i in range(BAUD_RATE):
                    output_pin.value(1)  # Set tone 2
                    utime.sleep_us(int(1e6 / (TONE_2_FREQ * 2)))
                    output_pin.value(0)  # Clear tone 2
                    utime.sleep_us(int(1e6 / (TONE_2_FREQ * 2)))

# Main loop to receive data and generate AFSK signal
while True:
    data = client_socket.recv(1024)
    if not data:
        break
    afsk(data)

# Clean up
client_socket.close()
server_socket.close()
