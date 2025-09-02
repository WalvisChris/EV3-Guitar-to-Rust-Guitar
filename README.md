# EV3-Guitar-to-Rust-Guitar
The game and webcam are recorded at the same time:  
[![Watch the video](https://img.youtube.com/vi/-0u0-XY2agc/0.jpg)](https://www.youtube.com/watch?v=-0u0-XY2agc)  

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

For page 10 in the original instruction, you want to connect the sensor to the other side of the ev3 brick (also mirror the parts at the bottom of the brick):
![1_1x](https://github.com/user-attachments/assets/7c4c7c63-d35f-461d-b793-e9dc3d5689e5)

For page 11-14 we will build a different connection because we need to leave room for the WIFI dongle and sd card:
![2_1x](https://github.com/user-attachments/assets/ef885fd6-dbc8-44a0-963a-bed0e9d475bb)
![3_1x](https://github.com/user-attachments/assets/d420552d-deaf-469c-8463-562ac5638993)
![4_1x](https://github.com/user-attachments/assets/b49627d9-63a2-4aaf-a314-11e1b364b8a8)
![5_1x](https://github.com/user-attachments/assets/21cca239-288c-44c1-8439-46ba83836efc)
![6_1x](https://github.com/user-attachments/assets/45225d34-ec93-4f16-9e17-26b84dfed3b7)
![7_1x](https://github.com/user-attachments/assets/7fd02d4f-72c8-4c07-952d-726e17912f7c)
![8_1x](https://github.com/user-attachments/assets/8a62fcfe-e224-47b6-8bd5-7ab6d25c7583)

On page 15 you can leave out the motor and the red parts. You just need the 7x5 gray plate and the blue and black connectors. Once you get to the part when you will connect it to the brick this is how to do that:
![9_1x](https://github.com/user-attachments/assets/ce1c94a7-9f3b-4b69-a78b-aa20a40ed235)
![10_1x](https://github.com/user-attachments/assets/ca98080a-aaa9-4227-8e3c-c31184cdd775)
![11_1x](https://github.com/user-attachments/assets/fce36367-1be6-4f3b-bb5b-6621dccb522f)
![12_1x](https://github.com/user-attachments/assets/9fd7989e-3fff-4f5b-8871-7e1482d90d8b)
![13_1x](https://github.com/user-attachments/assets/b90e6876-dfe0-4cd1-be0a-883ea90dd5d0)

The rest of the guitar will be build the exact same way as the instructions.

# Caveats
- cpufreq overclocking is **NOT** required.
- USB can be used instead of WIFI but it requires changes in the code.
