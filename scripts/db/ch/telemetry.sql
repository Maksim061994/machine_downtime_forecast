CREATE TABLE IF NOT EXISTS hakaton.telemetry
(
    dt      DATETIME,
    machine_number UInt16,
    vibration_on_support_1 Nullable(Float64),
    vibration_on_support_2 Nullable(Float64),
    vibration_on_support_3 Nullable(Float64),
    vibration_on_support_4 Nullable(Float64),
    oil_pressure_system Nullable(Float64),
    oil_temp_oil_block Nullable(Float64),
    oil_temp_system Nullable(Float64),
    bearing_temp_on_support_1 Nullable(Float64),
    bearing_temp_on_support_2 Nullable(Float64),
    bearing_temp_on_support_3 Nullable(Float64),
    bearing_temp_on_support_4 Nullable(Float64),
    rotor_current_1 Nullable(Float64),
    rotor_current_2 Nullable(Float64),
    stator_current_2 Nullable(Float64)
)
ENGINE = MergeTree
ORDER BY (dt, machine_number)