# SWLS Resonant Converter Sirius
list_soft_interlocks = [
    "DCCT 1 Fault",
    "DCCT 2 Fault",
    "DCCT High Difference",
    "Load Feedback 1 Fault",
    "Load Feedback 2 Fault",
]

list_hard_interlocks = [
    "Load Overcurrent",
    "DCLink Overvoltage",
    "DCLink Undervoltage",
    "Welded Contactor K1 Fault",
    "Welded Contactor K2 Fault",
    "Opened Contactor K1 Fault",
    "Opened Contactor K2 Fault",
    "External Interlock",
    "IIB Interlock",
]

list_iib_interlocks = [
    "Input Overvoltage",
    "Output Overvoltage",
    "Input Overcurrent",
    "Output Overcurrent",
    "Transformer and PFC Heat-Sink Overtemperature",
    "Output Inductor Overtemperature",
    "Diodes Heat-Sink Overtemperature",
    "Clamp Heat-Sink Overtemperature",
    "Driver MOSFETs and Auxiliary Board Overvoltage",
    "Driver MOSFETs Overcurrent",
    "Driver Flag High Switch Error",
    "Driver Flag Low Switch Error",
    "Auxiliary Board Overcurrent",
    "High Leakage Current",
    "Board IIB Overtemperature",
    "Module Overhumidity",
    "Contactor K1 Overcurrent",
    "Contactor K1 Open",
    "Contact Sticking of Contactor K1",
    "Contactor K2 Open",
    "Contact Sticking of Contactor K2",
    "Emergency Button",
]

list_iib_alarms = [
    "Input Overvoltage",
    "Output Overvoltage",
    "Input Overcurrent",
    "Output Overcurrent",
    "Transformer and PFC Heat-Sink Overtemperature",
    "Output Inductor Overtemperature",
    "Diodes Heat-Sink Overtemperature",
    "Clamp Heat-Sink Overtemperature",
    "Driver MOSFETs and Auxiliary Board Overvoltage",
    "Driver MOSFETs Overcurrent",
    "Auxiliary Board Overcurrent",
    "High Leakage Current",
    "Board IIB Overtemperature",
    "Module Overhumidity",
]

bsmp = {
    "ps_alarms": {"addr": 33, "format": "I", "size": 4, "egu": ""},
    "i_load_mean": {"addr": 34, "format": "f", "size": 4, "egu": "A"},
    "i_load_1": {"addr": 35, "format": "f", "size": 4, "egu": "A"},
    "i_load_2": {"addr": 36, "format": "f", "size": 4, "egu": "A"},
    "i_load_error": {"addr": 37, "format": "f", "size": 4, "egu": "A"},
    "v_dclink": {"addr": 38, "format": "f", "size": 4, "egu": "V"},
    "freq_modulated": {"addr": 39, "format": "f", "size": 4, "egu": "Hz"},
    "freq_modulated_compens": {"addr": 40, "format": "f", "size": 4, "egu": "Hz"},
    "v_input_iib": {"addr": 41, "format": "f", "size": 4, "egu": "V"},
    "v_output_iib": {"addr": 42, "format": "f", "size": 4, "egu": "V"},
    "i_input_iib": {"addr": 43, "format": "f", "size": 4, "egu": "A"},
    "i_output_iib": {"addr": 44, "format": "f", "size": 4, "egu": "A"},
    "temp_heatsink_transformer_pfc_iib": {"addr": 45, "format": "f", "size": 4, "egu": "°C"},
    "temp_output_inductor_iib": {"addr": 46, "format": "f", "size": 4, "egu": "°C"},
    "temp_heatsink_diodes_iib": {"addr": 47, "format": "f", "size": 4, "egu": "°C"},
    "temp_heatsink_clamp_iib": {"addr": 48, "format": "f", "size": 4, "egu": "°C"},
    "v_driver_and_aux_board_iib": {"addr": 49, "format": "f", "size": 4, "egu": "V"},
    "i_driver_iib": {"addr": 50, "format": "f", "size": 4, "egu": "A"},
    "i_aux_board_iib": {"addr": 51, "format": "f", "size": 4, "egu": "A"},
    "i_leakage_iib": {"addr": 52, "format": "f", "size": 4, "egu": "A"},
    "temp_board_iib": {"addr": 53, "format": "f", "size": 4, "egu": "°C"},
    "rh_iib": {"addr": 54, "format": "f", "size": 4, "egu": "%"},
    "iib_interlocks": {"addr": 55, "format": "I", "size": 4, "egu": ""},
    "iib_alarms": {"addr": 56, "format": "I", "size": 4, "egu": ""},
}