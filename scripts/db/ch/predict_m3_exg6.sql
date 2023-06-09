CREATE TABLE IF NOT EXISTS hakaton.predict_m3_exg7
(
    dt      DATETIME,
    motor Nullable(UInt32),
    housing Nullable(UInt32),
    valve Nullable(UInt32),
    support_bearing_2 Nullable(UInt32),
    gas_valve_reducer Nullable(UInt32),
    thrust_bearing Nullable(UInt32),
    sapphire_sensor_22_MDD_collector_pressure Nullable(UInt32),
    oil_tank Nullable(UInt32),
    support_bearing_1 Nullable(UInt32),
    coupling_cover Nullable(UInt32),
    rotor Nullable(UInt32),
    transformer_TM_4000_10_6 Nullable(UInt32),
    electrical_equipment_EXG_6 Nullable(UInt32),
    oil_cooler_M_05_1 Nullable(UInt32),
    sapphire_sensor_22_MDD_cyclone_pressure_drop Nullable(UInt32),
    working_oil_pump Nullable(UInt32),
    gas_valve_EXG_6 Nullable(UInt32),
    exhauster_EXG_6 Nullable(UInt32),
    support_bearing Nullable(UInt32),
    thyristor_exciter_TV_400_EXG_6_WU1 Nullable(UInt32),
    starter_oil_pump_motor Nullable(UInt32),
    gear_oil_pump_EXG_6 Nullable(UInt32),
    vibroconverter_VK_310S_EXG_6_T3 Nullable(UInt32),
    oil_pipes_EXG_6 Nullable(UInt32),
    CL1_TR_6_to_ED_EXG_6 Nullable(UInt32),
    CL2_TR_6_to_ED_EXG_6 Nullable(UInt32),
    vibroconverter_VK_310S_EXG_6_T2 Nullable(UInt32),
    equip_with_anomaly Nullable(UInt32)
)
ENGINE = MergeTree
ORDER BY (dt)