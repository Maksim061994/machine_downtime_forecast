CREATE TABLE IF NOT EXISTS hakaton.predict_m1_to_failure
(
    dt      DATETIME,
    machine_number UInt16,
    time_to_m1_seconds Nullable(FLOAT)
)
ENGINE = MergeTree
ORDER BY (dt, machine_number)