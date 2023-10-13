# esp32-afsk-modem
This repository qill have my code to generate and decode afsk message using an ESP32

## AFSK generator
Here's a high-level overview of the steps you'll need to follow:

    Import required libraries and set up the ESP32 for Wi-Fi communication.
    Set up the serial communication to receive data from the external device.
    Implement the AFSK modulation to convert the serial data to two tones (e.g., 1200Hz and 2200Hz) following the Bell 202 standard.
    Use PWM (Pulse Width Modulation) to generate audio signals at the specified tones.
    Connect a speaker or other audio output device to the output pin.
    Continuously read the serial data, modulate it to audio tones, and output it to the speaker.

## AFSK decoder
In this code:

    Include the necessary libraries for Wi-Fi, audio input, and the AFSK decoder.
    Set up Wi-Fi credentials and connect to the Wi-Fi network.
    Initialize the audio input and AFSK decoder.
    Create a connection to the computer over Wi-Fi using a client socket.
    In the loop, continuously read audio data and feed it to the AFSK decoder.
    When a valid AFSK data packet is decoded, send it to the computer over Wi-Fi.
    Check the Wi-Fi connection and reconnect if necessary.

You will need to customize this code to match your specific hardware setup and computer's IP address. Additionally, you'll need to implement the AFSK signal processing and adapt it to your specific requirements.

Please note that this code provides a basic framework and does not include the complete AFSK decoding logic, as that can be quite complex. You may need to incorporate additional libraries or implement the AFSK decoding algorithm based on the Bell 202 standard.
