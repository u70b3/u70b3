# Hi, I'm Kid 👋

I contribute to query engines and lakehouse storage, focusing on **correctness
across system boundaries**: durable writes, native APIs, and consistent query
results. I work primarily in **Rust and C++**, with Java contributions to Doris
and Paimon.

## Selected work

- **Concurrency correctness** — Fixed publication ordering in
  [DuckDB's parallel hash-join build](https://github.com/duckdb/duckdb/pull/24884)
  and [Paimon C++'s singleton initialization](https://github.com/apache/paimon-cpp/pull/203).
- **Durable state & recovery** — Added the
  [Doris × Lance index-job state-machine foundation](https://github.com/apache/doris/pull/67235),
  with fencing for unknown mutation outcomes and failover replay.
- **Query correctness** — Restored complete results in
  [Lance scans after cross-generation updates and deletes](https://github.com/lance-format/lance/pull/7917)
  and preserved [all-NULL groups in DataFusion TopK](https://github.com/apache/datafusion/pull/23684)
  with guarded optimization and bounded state within TopK; kept
  [DuckDB's `decode` from mutating shared input buffers](https://github.com/duckdb/duckdb/pull/24353).
- **Native APIs & ownership** — Added panic-to-error handling for
  [lance-c calls and Arrow streams](https://github.com/lance-format/lance-c/pull/62)
  and hardened [callback and waker lifetimes](https://github.com/lance-format/lance-c/pull/65);
  delivered [bounded JNI index-metadata reads with task-owned allocators in Doris](https://github.com/apache/doris/pull/66637).
- **Index infrastructure** — Exposed
  [shared-model, uncommitted index-segment builds for C/C++ workers](https://github.com/lance-format/lance-c/pull/57)
  and enabled [Parquet `INTERVAL` Bloom pruning with versioned writer/reader compatibility](https://github.com/duckdb/duckdb/pull/24277).
- **Cross-engine time travel** — Implemented
  [watermark-based batch reads in Paimon Rust](https://github.com/apache/paimon-rust/pull/677)
  and fixed [Java snapshot searches over histories with missing watermarks](https://github.com/apache/paimon/pull/9037).

I also work on measured performance improvements, including
[vectorizing Comet's `spark_unscaled_value`](https://github.com/apache/datafusion-comet/pull/4972)
(reported **9.3–11.7×** in 8,192-row expression microbenchmarks).

<!-- contribution-stats:start -->
Selected upstream contributions: 58 merged pull requests across 15 repositories in the Apache, DuckDB and Lance ecosystems.
<!-- contribution-stats:end -->

[Browse public upstream PRs →](https://github.com/search?q=is%3Apr+author%3Au70b3+is%3Amerged+org%3Aapache+org%3Aduckdb+org%3Alance-format+org%3Alancedb&type=pullrequests)
· [lucian1412@outlook.com](mailto:lucian1412@outlook.com)
