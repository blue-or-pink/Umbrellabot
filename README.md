# Author: Jay

To set up Umbrellabot, you must be using the Freenove framework on Raspberry Pi, and have gpiozero installed. The other classes for servo & watersensor are stored in the project already.
</div>
For mechanisms, you must have an external switch, a servo, a motion sensor, and a TFW-RN1 water sensor connected to the Pi through an ADC.
</div>
You must also verify your i2c smbus addresses for your ADC; run <i2cdetect -y 1> in your terminal and a grid will appear - replace <0x40> & <0x48> in lines 7-11 in <waterSensor.py>, as well as line 9 in <PCF8591.py> with the addresses that show up in your grid. (there should be at least 2, one for your pi and one for your ADC)
</div>
To run the program, since every file branches off from <main.py>, just simply run <python main.py> while connected to the Raspberry Pi. 


# also P.S. i dont know HTLM i just used "<>" where they looked cool