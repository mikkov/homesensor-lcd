Installation
============
git clone https://github.com/mikkov/homesensor-lcd

apt-get install python2.7 python-usb

You may need to copy the provided `99-lcdsysinfo.rules` file into
`/etc/udev/rules.d/` in order to grant pylcdsysinfo permission to claim the device without running as root.

Example:

    sudo cp 99-lcdsysinfo.rules /etc/udev/rules.d/

If the screen is already plugged in, unplug and plug back in again after copying the udev rules file.

pylcdsysinfo relies on the Python USB library http://pyusb.sourceforge.net/ - this can be installed via pip/easy_install


Usage
=====
python homesensor-lcd.py
