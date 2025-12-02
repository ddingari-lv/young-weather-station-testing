import pandas as pd
from datetime import datetime

def parse_wimwv(sentence):
    """Parse an NMEA WIMWV sentence into a structured DataFrame row."""
    if not sentence.startswith("$WIMWV"):
        raise ValueError("Not a valid WIMWV sentence")
    data, checksum = sentence[7:].split('*')
    fields = data.split(',')
    parsed_data = {
        'Wind_angle_deg': float(fields[0]) if fields[0] else None,
        'Reference': fields[1],
        'Wind_speed': float(fields[2]) if fields[2] else None,
        'Wind_speed_units': fields[3],
        'Status': fields[4],
    }
    return pd.DataFrame([parsed_data])

def parse_yxxdr(sentence):
    """Parse an NMEA YXXDR sentence into a structured DataFrame row."""
    if not sentence.startswith("$YXXDR"):
        raise ValueError("Not a valid YXXDR sentence")
    data, checksum = sentence[7:].split('*')
    fields = data.split(',')
    parsed_data = {
        'Relative_wind_chill_temp_C': float(fields[1]) if fields[1] else None,
        'Relative_wind_chill_unit': fields[2],
        'Relative_wind_chill_ID': fields[3],
        'Theoretical_wind_chill_temp_C': float(fields[5]) if fields[5] else None,
        'Theoretical_wind_chill_unit': fields[6],
        'Theoretical_wind_chill_ID': fields[7],
        'Heat_index_temp_C': float(fields[9]) if fields[9] else None,
        'Heat_index_unit': fields[10],
        'Heat_index_ID': fields[11],
        'Barometric_pressure_bars': float(fields[13]) if fields[13] else None,
        'Barometric_pressure_unit': fields[14],
    }
    return pd.DataFrame([parsed_data])

def parse_wimda(sentence):
    """Parse an NMEA WIMDA sentence into a structured DataFrame row."""
    if not sentence.startswith("$WIMDA"):
        raise ValueError("Not a valid WIMDA sentence")
    data, checksum = sentence[7:].split('*')
    fields = data.split(',')
    parsed_data = {
        'Barometric_pressure_inHg': float(fields[0]) if fields[0] else None,
        'Pressure_unit_inHg': fields[1],
        'Barometric_pressure_bars': float(fields[2]) if fields[2] else None,
        'Pressure_unit_bars': fields[3],
        'Air_temperature_C': float(fields[4]) if fields[4] else None,
        'Temperature_unit_air': fields[5],
        'Water_temperature_C': float(fields[6]) if fields[6] else None,
        'Temperature_unit_water': fields[7],
        'Relative_humidity_percent': float(fields[8]) if fields[8] else None,
        'Absolute_humidity_percent': float(fields[9]) if fields[9] else None,
        'Dew_point_C': float(fields[10]) if fields[10] else None,
        'Dew_point_unit': fields[11],
        'Wind_direction_true': float(fields[12]) if fields[12] else None,
        'Wind_direction_unit_true': fields[13],
        'Wind_direction_magnetic': float(fields[14]) if fields[14] else None,
        'Wind_direction_unit_magnetic': fields[15],
        'Wind_speed_knots': float(fields[16]) if fields[16] else None,
        'Wind_speed_unit_knots': fields[17],
    }
    return pd.DataFrame([parsed_data])

def parse_wixdr(sentence):
    """Parse an NMEA WIXDR sentence into a structured DataFrame row."""
    if not sentence.startswith("$WIXDR"):
        raise ValueError("Not a valid WIXDR sentence")
    data, checksum = sentence[7:].split("*")
    fields = data.split(",")
    parsed_data = {}

    # The fields in WIXDR are a repeating set of four:
    # 1. Transducer type (C=Temperature, H=Humidity, P=Pressure)
    # 2. Measurement value
    # 3. Units
    # 4. Transducer ID

    # Example sentence: $WIXDR,C,22.6,C,TEMP,H,43.4,P,RH,P,1.0211,B,BARO*4A

    
    for i in range(0, len(fields) - 3, 4):
        transducer_type = fields[i]
        value = float(fields[i + 1]) if fields[i + 1] else None
        units = fields[i + 2]
        transducer_id = fields[i + 3]

        if transducer_type == "C":
            parsed_data["Temperature_C"] = value
            parsed_data["Temperature_unit"] = units
        elif transducer_type == "H":
            parsed_data["Relative_humidity_percent"] = value
            parsed_data["Humidity_unit"] = units
        elif transducer_type == "P":
            parsed_data["Barometric_pressure"] = value
            parsed_data["Pressure_unit"] = units
        else:
            print(
                f"Warning: Unknown transducer type '{transducer_type}' in WIXDR sentence."
            )

    return pd.DataFrame([parsed_data])


def parse_nmea_sentence(sentence):
    """Parse an NMEA sentence and return a structured DataFrame row with a timestamp."""
    if sentence.startswith("$WIMWV"):
        parsed_data = parse_wimwv(sentence)
    elif sentence.startswith("$WIMDA"):
        parsed_data = parse_wimda(sentence)
    elif sentence.startswith("$YXXDR"):
        parsed_data = parse_yxxdr(sentence)
    elif sentence.startswith("$WIXDR"):
        parsed_data = parse_wixdr(sentence)
    else:
        raise ValueError(f"Unsupported NMEA sentence type: {sentence}")
    
    # Add a timestamp as the index
    parsed_data.index = [datetime.now()]
    return parsed_data