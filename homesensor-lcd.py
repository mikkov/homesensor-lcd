#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from pylcdsysinfo import BackgroundColours, COL2LEFT, TextColours, TextAlignment, TextLines, LCDSysInfo
import urllib
import json
import time
import unicodedata
import ConfigParser

class Screen():
    def __init__(self):
        self.lcd = LCDSysInfo()
        self.lcd.clear_lines(TextLines.ALL, BackgroundColours.BLACK)
        self.lcd.dim_when_idle(False)
        self.lcd.set_brightness(127)
        self.lcd.save_brightness(127, 127)

    def clear(self):
        self.lcd.clear_lines(TextLines.ALL, BackgroundColours.BLACK)

    def printc(self, data, sensors_to_display):
        line = 1
        for key in sensors_to_display:
            for sensor in data:
                if sensor['id'] == key:
                    value = str(sensor['value'])
                    txt = unicode(sensor['name'] + "\t " + value + "" + sensor['unit'])
                    txt = txt.replace(u"\u00B0", "^")
                    txt = unicodedata.normalize('NFKD', txt).encode('ascii', 'ignore')
                    print(txt)
                    self.lcd.display_text_on_line(line, txt, False, TextAlignment.LEFT, TextColours.LAVENDER)
                    line +=1

def read_config(filename):
    config = ConfigParser.ConfigParser()
    config.read(filename)
    conf = {}
    conf['url'] = config.get("Server", "url")
    conf['sensors'] = json.loads(config.get("Display", "sensors"))
    return conf

def get_values(url):
    f = urllib.urlopen(url)
    data = f.read()
    f.close()
    return json.loads(data)

def main():
    screen = Screen()
    config = read_config("config.ini")
    while True:
        try:
            content = get_values(config['url'])
            screen.printc(content, config['sensors'])
        except:
            pass
        time.sleep(30)


if __name__ == "__main__":
    main()
