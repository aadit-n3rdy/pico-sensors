# ASC Pico IoT Board

A GitHub Repository for the IoT end device board for the RPi Pico, developed by students from 
Amrita School of Computing, Amrita Vishwa Vidyapeetham, Coimbatore. 

![Amrita Vishwa Vidyapeetham, Coimbatore](https://upload.wikimedia.org/wikipedia/en/f/f8/Amrita-vishwa-vidyapeetham-color-logo.png)

## Raspberry Pi Pico
![Raspberry Pi Pico Development Board made by ASC-CSE](assets/pico.jpeg) | ![Raspberry Pi Pico Development Board made by ASC-CSE with better pin headers](assets/with_headers.jpeg) | ![Raspberry Pi Pico connected to PC via USB](assets/with_usb.jpeg)
----|---|---
-------
The Raspberry Pi Pico is a low cost microcontroller. It uses GPIO pins to
interface with various sensors and actuators, and can be used for embedded systems and IoT
projects.

The Raspberry Pi Pico can be programmed using the MicroPython language or the official 
[C/C++ SDK](https://www.raspberrypi.com/documentation/microcontrollers/c_sdk.html) 
provided by the Raspberry Pi Foundation for the Pico. 

The ASC Pico IoT Board addresses a few issues of the Raspbery Pi Pico, in the 
following ways:
- 5V output pin is added for easy connection of various 5V sensors
- Female jumper headers are soldered to make it much easier to connect sensors and jumper wires

The board also has a few differences from the Pico's pinout:
- The default UART communications (Pin 1 and 2 on the Pico) are on dedicated Rx and Tx pins.
- The pins have a different order, and are labeled for easy identification.
- The digital pins are on the right side of the board, and analog pins are on the left side.

## Compilation Instructions

### For C/C++: 

1. Install CMake, and the GCC ARM compiler. On Ubuntu, the command is as follows:
```bash
sudo apt-get update
sudo apt-get install cmake gcc-arm-none-eabi libnewlib-arm-none-eabi build-essential libstdc++-arm-none-eabi-newlib
```

2. Clone the repository 
```bash
git clone https://github.com/aadit-n3rdy/asc-pico-iot-board.git
cd pico-sensor
git submodule update --init --recursive
```

3. Set the env `PICO_SDK_PATH` environment variable
```bash
export PICO_SDK_PATH=`pwd`/pico-sdk
```

4. Create a build directory, and build the examples
```bash
mkdir build
cd build
cmake ..
```

5. Open any of the folders in the build directory, and build the .uf2 file. The following is
a demonstration for the `blink` example
```bash
cd blink
make -j4
```

6. Load the .uf2 file and execute it on the Raspberry Pi Pico 
(refer [Getting started with Raspberry Pi Pico](https://datasheets.raspberrypi.com/pico/getting-started-with-pico.pdf), 
section 3.2, for information on loading the .uf2 file)


### MicroPython:
1. The Thonny IDE is used. [Install Thonny](https://thonny.org/).
2. The instructions to install MicroPython firmware on the Pico are available on the [official website](https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/3)
3. Once the firmware has been installed, MicroPython code can be executed on the Raspberry Pi Pico using the Thonny IDE

## Contributors

- E. Aadithyaa - CB.EN.U4CSE22114
- Ananthakrishnan Balajee - CB.EN.U4CSE22206
- Srivatsan S. - CB.EN.U4CSE22249
- Jeet Thakur - CB.EN.U4CSE22518

Under the guidance of our mentor:  
Dr. V Ananthanarayanan,   
Associate Professor,  
School of Computing,  
Amrita Vishwa Vidyapeetham, Coimbatore
