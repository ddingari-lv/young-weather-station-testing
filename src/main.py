import serial
from serial_read import open_serial_port, close_serial_port
from nmea_convert import parse_nmea_sentence

# Serial port configuration
SERIAL_PORT = 'COM7'  # Update this to your serial port
BAUDRATE = 4800

# Initialize data list to store parsed data
data_list = []

try:
    # Open serial port
    ser = open_serial_port(SERIAL_PORT, BAUDRATE)

    # Continuously read from the serial port
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('ascii', errors='replace').strip()
            print(f"Received: {line}")
            
            try:
                parsed_data = parse_nmea_sentence(line)
                data_list.append(parsed_data)
                print(f"Parsed Data:\n{parsed_data}\n")
            except ValueError as e:
                print(f"Error parsing sentence: {e}")

except KeyboardInterrupt:
    print("Stopping data read...")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close serial port
    close_serial_port(ser)
    print("Final collected data:")
    for entry in data_list:
        print(entry)