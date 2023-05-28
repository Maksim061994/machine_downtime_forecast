CREATE TABLE IF NOT EXISTS hakaton.predict_m1
(
    dt_start      DATETIME,
    dt_end      DATETIME,
    machine_number UInt16,
    preds_proba Nullable(Float64),
    preds_label Nullable(UInt64)
)
ENGINE = MergeTree
ORDER BY (dt_start, dt_end, machine_number)