import serial

def open_serial_port(port, baudrate=4800, timeout=1):
    """Open and return a serial port connection."""
    ser = serial.Serial(port, baudrate, timeout=timeout)
    print(f"Connected to {port} at {baudrate} baud.")
    return ser

def close_serial_port(ser):
    """Close the given serial port connection."""
    ser.close()
    print("Serial port closed.")

