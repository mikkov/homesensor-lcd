#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from pylcdsysinfo import BackgroundColours, COL2LEFT, TextColours, TextAlignment, TextLines, LCDSysInfo
import urllib
import json

class Screen():
    def __init__(self):
        self.lcd = LCDSysInfo()
        self.lcd.clear_lines(TextLines.ALL, BackgroundColours.BLACK)
        self.lcd.dim_when_idle(False)
        self.lcd.set_brightness(255)
        self.lcd.save_brightness(127, 255)

    def clear(self):
        self.lcd.clear_lines(TextLines.ALL, BackgroundColours.BLACK)

    def printc(self, data):
        for line,sensor in enumerate(data):
            try:
                value = sensor['value']
            except:
                value = str(sensor['value'])

            txt = sensor['name'] + ": " + value + "" + sensor['unit']
            print(txt)
            self.lcd.display_text_on_line(line+1, txt, False, None, TextColours.GREEN)

def read_config():
    return {'url': 'http://localhost/homesensor/sensor.php'}

def get_values(url):
    f = urllib.urlopen(url)
    data = f.read()
    f.close()
    return json.loads(data)

if __name__ == "__main__":
    screen = Screen()
    config = read_config()
    content = get_values(config['url'])
    screen.printc(content)
