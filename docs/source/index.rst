SunFounder PiPower Module
=================================

.. image:: img/media1.png
    :width: 600

* Pass Through Charging
* Shutdown Current：< 0.5mA
* Input:
    * USB Type-C, 5V/3A
    * Battery Input
* Output：
    * USB Type-A, 5V/3A
    * 2x4P P2.54 pin headers

* Charging Power：7.4V/1A 7.4W
* Equipped Battery
    * Type: 3.7V Lithium-ion batteries x 2
    * Capacity: 2000mAh
    * Connector: PH2.0, 5P
* Over Discharge Protection Voltage：3.2V
* Overcharge Protection Voltage：4.2V
* Dimension: 90mm x 60mm x 24.9mm
* On-board Indicators
    * 1 x Charging Indicator (CHG)
    * 1 x Power Indicator (PWR)
    * 4 Battery Indicators (D4 ~ D7)


PiPower is a power supply module for Raspberry Pi with recharging function. 
It can output 5V/3A power supply to meet various Raspberry Pi usage situation. 
It has 4 power indicators; each indicator represents 25% of the power, and is equipped with a power switch to turn on/off the power of the Raspberry Pi without plugging or unplugging the power cord.

When the battery power is low, you can insert a 5V/3A Type-C cable to charge the batteries, and the charging indicator will light up and turn off when fully charged.

.. warning::
    When you put the battery in for the first time or when the battery is unplugged and put in again, the battery will not work properly, at this time, you need to plug the Type C cable into the charging port to turn off the protection circuit, and the battery can be used normally.




.. toctree::
    components
    assemble
    features
    faq
