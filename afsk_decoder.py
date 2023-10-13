#include <Arduino.h>
#include <WiFi.h>
#include <Audio.h>
#include <ToneDecoder.h>

const char* ssid = "YourWiFiSSID";
const char* password = "YourWiFiPassword";
const char* host = "your-computer-ip-address";
const int port = 12345; // The port on your computer to receive data

AudioInputI2S audioInput;
ToneDecoder toneDecoder;
WiFiClient client;

void setup() {
  Serial.begin(115200);
  delay(1000);

  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");

  // Initialize the audio input
  audioInput.setGain(32);
  audioInput.begin();

  // Initialize the ToneDecoder for AFSK
  toneDecoder.begin(1200);

  // Connect to the computer over Wi-Fi
  if (client.connect(host, port)) {
    Serial.println("Connected to the computer over Wi-Fi");
  }
}

void loop() {
  // Read audio data
  audioInput.update();
  int16_t sample = audioInput.read();

  // Feed the sample to the AFSK decoder
  toneDecoder.processSample(sample);

  // Check if a valid data packet has been received
  if (toneDecoder.available()) {
    String decodedData = toneDecoder.getData();
    Serial.println("Decoded Data: " + decodedData);

    // Send the data to the computer over Wi-Fi
    client.println(decodedData);
  }

  // Check Wi-Fi connection and reconnect if necessary
  if (!client.connected()) {
    if (client.connect(host, port)) {
      Serial.println("Reconnected to the computer over Wi-Fi");
    }
  }
}
