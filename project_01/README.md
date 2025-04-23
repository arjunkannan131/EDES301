# Project BreatheSafe

**BreatheSafe** is a compact, bootable environmental monitoring device built on the PocketBeagle. It collects and displays air quality data from multiple I2C sensors on a 128x32 OLED screen using Python 3.11.

---

Hackster.io page: https://www.hackster.io/your-link-here](https://www.hackster.io/ak131/breathesafe-pocket-sized-environmental-monitor-d9377a

## 🌟 Features

- 🌡️ Real-time temperature and pressure from **BMP280**
- 🌫️ PM2.5 particulate data from **PMSA003I**
- 🧪 eCO₂ and TVOC air quality data from **CCS811**
- 🖥️ OLED display powered by **SSD1306**
- ⚡ Clean single-shot display behavior on startup (only runs once and exits)
- 🧠 Sensor-driven — display is only shown if PM2.5 data is non-zero

---

## 🧰 Hardware Required

- PocketBeagle
- BMP280 (I2C)
- PMSA003I (I2C)
- CCS811 (CJMCU-811, I2C)
- SSD1306 128x32 OLED Display (I2C)
- Breadboard + jumper wires
- 3.3V power rail

---

## 🧑‍💻 Software Build Instructions

1. Update System Packages
Ensure your system packages are up to date:

sudo apt update
sudo apt upgrade -y

2. Install Python 3.11 and pip
If Python 3.11 is not already installed, you can install it using the following commands:

sudo apt install -y software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install -y python3.11 python3.11-venv python3.11-dev

3. Install pip for Python 3.11:

curl -sS https://bootstrap.pypa.io/get-pip.py | sudo python3.11

3. Install Required Python Libraries
Install the necessary Python libraries using pip:

python3.11 -m pip install --upgrade pip
python3.11 -m pip install \
  adafruit-circuitpython-ssd1306 \
  adafruit-circuitpython-ccs811 \
  smbus2 \
  bmp280 \
  pillow
  
4. Enable I2C Interface
Ensure the I2C interface is enabled on your PocketBeagle:

sudo apt install -y i2c-tools

Verify connected I2C devices:

sudo i2cdetect -y -r 1

You should see addresses corresponding to your sensors and OLED display (e.g., 0x3C for the SSD1306 display).

5. Run the Script
Execute the main Python script:

python3.11 breathesafe.py

Upon execution, the script will:

Display "Starting..." on the OLED screen.

Wait for 5 seconds to allow sensors to stabilize.

Read data from the BMP280, PMSA003I, and CCS811 sensors.

Display temperature, pressure, and PM2.5 readings on the OLED screen.
