create table predict_m1
(
    dt_start       DateTime,
    dt_end         DateTime,
    machine_number UInt16,
    preds_proba Nullable(Float64),
    preds_label Nullable(UInt64),
    tm Nullable(String)
) engine = MergeTree ORDER BY (dt_start, dt_end, machine_number)
SETTINGS index_granularity = 8192;