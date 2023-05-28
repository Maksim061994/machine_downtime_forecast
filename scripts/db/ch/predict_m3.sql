CREATE TABLE IF NOT EXISTS hakaton.predict_m3
(
    dt      DATETIME,
    machine_number UInt16,
    tm UInt64,
    anomalies BOOL,
    probability_anomalies Nullable(Float64),
    model_version Nullable(UInt16)
)
ENGINE = MergeTree
ORDER BY (dt, machine_number)