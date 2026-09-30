# ADS1115 Software Oscilloscope

## Project Overview
This project uses an ADS1115 analog-to-digital converter (ADC) with a Raspberry Pi to read an analog voltage signal and display it as a continuously updating waveform using Python and Matplotlib.

The program reads voltage values from channel A0, stores them in a rolling buffer, and plots the readings against time. This provides a simple software oscilloscope for observing low-voltage signals.

## Hardware Requirements
- Raspberry Pi
- ADS1115 16-bit ADC module
- Breadboard and jumper wires
- Analog signal source (optional)
- Common ground connection for the signal source and circuit

## Software Requirements
- Python 3
- Thonny IDE (or another Python editor)
- NumPy
- Matplotlib
- Adafruit Blinka
- Adafruit CircuitPython ADS1x15 library

## Wiring Connections

| Raspberry Pi | ADS1115 |
|---|---|
| 3.3V | VDD |
| GND | GND |
| GPIO 2 (SDA1) | SDA |
| GPIO 3 (SCL1) | SCL |
| Analog signal output | A0 |

If using an external signal source, connect its signal ground to the common GND of the ADS1115 and Raspberry Pi.

**Safety note:** Keep the voltage applied to A0 within the ADS1115's permitted input range and never exceed the board's supply or input limits.

## Installation

Open a terminal on the Raspberry Pi and install the required packages:

```bash
python3 -m pip install numpy matplotlib adafruit-blinka adafruit-circuitpython-ads1x15
```

If your system uses a Python virtual environment, activate it before installing the packages and running the program.

## How to Run
1. Connect the ADS1115 to the Raspberry Pi according to the wiring table.
2. Connect the analog signal to A0, if you are using an external signal.
3. Open Thonny IDE.
4. Copy the Python program into a new file.
5. Save the file as `ads1115_oscilloscope.py`.
6. Run the program.
7. A Matplotlib window will open and display the live voltage plot.
8. Close the plot window to stop the program.

## Program Settings

| Setting | Default | Description |
|---|---:|---|
| `DURATION` | 10 seconds | Time span represented on the plot |
| `SAMPLE_RATE` | 128 SPS | Requested ADC data rate |
| `GAIN` | 1 | ADC gain setting (±4.096 V full-scale range) |
| `CHANNEL` | 0 | Reads analog input A0 |
| `I2C_ADDRESS` | `0x48` | Default I2C address of the ADS1115 |

## Working Principle
1. The program initializes the I2C connection between the Raspberry Pi and ADS1115.
2. The ADS1115 converts the analog input voltage on A0 into digital readings.
3. Each reading is retrieved as a voltage value.
4. The latest value is added to a fixed-size buffer, while older values are discarded.
5. Matplotlib updates the graph to show the changing voltage over time.
6. The plot continues updating until its window is closed.

## Troubleshooting
- **ADS1115 not detected:** Check VDD, GND, SDA, and SCL wiring. Confirm that I2C is enabled on the Raspberry Pi and verify the module's I2C address.
- **No waveform appears:** Check that the signal source is connected to A0 and that all grounds are common.
- **Missing Python modules:** Install the required packages in the same Python environment used to run the script.
- **Graph shows a flat line:** Confirm that the input signal is changing and that its voltage is within the ADC's supported range.

## Limitations
- This is a basic software oscilloscope intended for low-frequency signal observation and learning.
- The actual sampling and display rates may vary depending on the Raspberry Pi, Python environment, and plotting performance.
- It is not a replacement for a calibrated laboratory oscilloscope.

## Conclusion
The project demonstrates how a Raspberry Pi and ADS1115 can be used to acquire analog voltage readings and visualize them in real time with Python. It provides practical experience with I2C communication, analog-to-digital conversion, data buffering, and live plotting.
