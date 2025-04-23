import time
from smbus2 import SMBus
from bmp280 import BMP280
import board
import busio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont

# I2C Setup
i2c_display = busio.I2C(board.SCL, board.SDA)
bus = SMBus(1)

# Display config
WIDTH = 128
HEIGHT = 32
display = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c_display, addr=0x3C)

# Drawing setup
image = Image.new("1", (WIDTH, HEIGHT))
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()

# Clear and show "Starting..." immediately
draw.rectangle((0, 0, WIDTH, HEIGHT), outline=0, fill=0)
draw.text((0, 10), "Starting...", font=font, fill=255)
display.image(image)
display.show()

# Sensor setup
bmp280 = BMP280(i2c_dev=bus)
PMSA003I_ADDR = 0x12

# Read PM2.5
def read_pm25(bus):
    try:
        data = bus.read_i2c_block_data(PMSA003I_ADDR, 0x00, 32)
        pm2_5 = (data[12] << 8) | data[13]
        return pm2_5
    except:
        return 0

# Main
def main():
    print("Warming up sensors...")
    time.sleep(5)

    try:
        temperature = bmp280.get_temperature()
        pressure = bmp280.get_pressure()
    except:
        temperature, pressure = 0.0, 0.0

    pm2_5 = read_pm25(bus)

    if pm2_5 != 0:
        draw.rectangle((0, 0, WIDTH, HEIGHT), outline=0, fill=0)
        draw.text((0, 0), f"{temperature:.1f} C", font=font, fill=255)
        draw.text((0, 10), f"{pressure:.1f} hPa", font=font, fill=255)
        draw.text((0, 20), f"PM2.5: {pm2_5}", font=font, fill=255)
        display.image(image)
        display.show()
        print("Displayed:", temperature, pressure, pm2_5)
    else:
        print("PM2.5 is 0 — no display triggered.")

if __name__ == "__main__":
    main()
