CREATE TABLE IF NOT EXISTS hakaton.history_failures
(
    dt      DATETIME,
    machine_number UInt16,
    tm UInt64,
    name_tm String,
    type_work UInt64
)
ENGINE = MergeTree
ORDER BY (dt, machine_number)