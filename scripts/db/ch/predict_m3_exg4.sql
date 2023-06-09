CREATE TABLE IF NOT EXISTS hakaton.predict_m3_exg4
(
    dt      DATETIME,
    electric_motor Nullable(UInt32),
    bearing_support Nullable(UInt32),
    worm Nullable(UInt32),
    gas_valve_reducer Nullable(UInt32),
    working_oil_pump Nullable(UInt32),
    electrical_apparatus Nullable(UInt32),
    bearing_support_2 Nullable(UInt32),
    gate_valve Nullable(UInt32),
    gasoline Nullable(UInt32),
    vibrator_converter Nullable(UInt32),
    thermocouple_bearing_support Nullable(UInt32),
    rotor Nullable(UInt32),
    oil_cooler Nullable(UInt32),
    bearing_support_thrust Nullable(UInt32),
    exhaust_fan Nullable(UInt32),
    spare_parts_and_regulating_armature Nullable(UInt32),
    bearing_support_1 Nullable(UInt32),
    gas_valve_electric_motor Nullable(UInt32),
    contact_line_1 Nullable(UInt32),
    contact_line_2 Nullable(UInt32),
    tor_r_tm_4000_10_6 Nullable(UInt32),
    thyratron_exciter_vt_rem_400 Nullable(UInt32),
    oil_pipes_exhaust_fan Nullable(UInt32),
    equip_with_anomaly Nullable(UInt32)
)
ENGINE = MergeTree
ORDER BY (dt)