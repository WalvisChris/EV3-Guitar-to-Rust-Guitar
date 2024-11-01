# Instructions
1) Install the ev3dev2 firmware to the EV3 Brick: https://www.ev3dev.org/docs/getting-started/
2) Connect EV3 Brick to the same wifi network as your computer.
3) Install the 'python-ev3dev2' library to your computer (> pip install python-ev3dev2).
4) Install the 'pynput' library to your computer (> pip install pynput).
5) In 'guitar.py' and 'input.py' change HOST to your local ipv4 adress (cmd > ipconfig).
6) In 'guitar.py' and 'input.py' change PORT to any open communication port (65432).
7) Download 'guitar.py' to the EV3 Brick.
8) Join yout Rust game (since this takes a long time).
9) Run the 'input.py' first on your computer.
10) Grab a acoustic guitar and press "R" to play the guitar.
11) Run the 'guitar.py' on the EV3 Brick.
12) Use 1 hand to determine the note and the other hand to press the strings of the guitar.

# Design

For extra fun, you can try to make a realistic lego technic guitar. You can base it off the EV3 guitar instructions, however you will need to change it a bit since it doens't leave space for the USB port which is needed for a WIFI or USB connection.

**EV3 Guitar Instructions:**
https://www.lego.com/cdn/product-assets/product.bi.additional.extra.pdf/31313_X_EL3CTRIC%20GUITAR.pdf

# Caveats
- cpufreq overclocking is **NOT** required.
- USB can be used instead of WIFI but it requires changes in the code.
