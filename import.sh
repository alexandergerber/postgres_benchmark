 timescaledb-parallel-copy \
--db-name test_db \
--table test_table \
--file test_data.csv \
--connection "host=localhost port=5433 user=timescale password=timescale" \
--workers 2
