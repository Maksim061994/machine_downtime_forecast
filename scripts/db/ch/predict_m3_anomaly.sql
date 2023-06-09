CREATE TABLE IF NOT EXISTS hakaton.predict_m3_anomaly
(
    dt      DATETIME,
    machine_number UInt16,
    number_anomaly Nullable(UInt32)
)
ENGINE = MergeTree
ORDER BY (dt, machine_number)