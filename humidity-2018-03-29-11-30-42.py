# This file has been written to your home directory for convenience. It is
# saved as "/home/pi/humidity-2018-03-29-11-30-42.py"

from sense_emu import SenseHat

sense = SenseHat()

green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)
pixels = list(range(64))
while True:
    humidity = sense.humidity
    humidity_value = 64 * humidity / 100
    temperature = sense.temperature
    temperature_value = 64 * (temperature + 30 )/ 135
    pressure = sense.pressure
    pressure_value = 64 * (pressure - 260)/ 1000
    for i in range(64):
        pixels[i] = white
        if i < max( humidity_value, temperature_value, pressure_value):   
            pixels[i]= (0, 255, 255)
        if i < min( humidity_value, temperature_value, pressure_value):
            pixels[i]= black
        if i == round(humidity_value):
            pixels[i] = green
        if i == round(temperature_value):
            pixels[i] = red  
        if i == round(pressure_value):
            pixels[i] = blue
    ##pixels = [green if i < humidity_value else white for i in range(64)]
    sense.set_pixels(pixels)
