CREATE TABLE IF NOT EXISTS hakaton.predict_m3_anomaly_equip
(
    dt      DATETIME,
    machine_number UInt16,
    equip Nullable(String),
    number_anomaly Nullable(UInt32)
)
ENGINE = MergeTree
ORDER BY (dt, machine_number)