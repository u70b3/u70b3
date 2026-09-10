# Hi, I'm Kid 👋

Open-source data systems contributor working at the boundaries between query engines,
lakehouse formats, and index infrastructure — turning correctness, durability, and
performance problems into tested upstream changes in **Rust and C++**.

- **Durability & correctness** — WAL generations and fencing, object-store and cache
  lifetimes, weak-memory concurrency, safe FFI boundaries, NULL and overflow semantics.
- **Index & query behavior** — HNSW/IVF alignment against the literature, SQL and
  Parquet semantics, vectorized Arrow execution.
- **Lakehouse interoperability** — Iceberg, Paimon and DuckLake metadata and time travel.

## Selected work

- **Durable state & distributed jobs** — [Doris × Lance index job lifecycle with fence,
  quota and edit-log replay](https://github.com/apache/doris/pull/67235), on
  [JNI metadata reads with explicit native-allocator ownership](https://github.com/apache/doris/pull/66637).
- **Cross-language boundaries** — [a panic firewall across 66 C entry points](https://github.com/lance-format/lance-c/pull/62),
  and [distributed segment build APIs that share one trained model across fragments](https://github.com/lance-format/lance-c/pull/57).
- **Engine semantics** — [Parquet `INTERVAL` Bloom pruning](https://github.com/duckdb/duckdb/pull/24277),
  [input immutability in `decode`](https://github.com/duckdb/duckdb/pull/24353), a
  [mixed-engine watermark bug found and fixed upstream](https://github.com/apache/paimon/pull/9037),
  and [vectorized decimal execution](https://github.com/apache/datafusion-comet/pull/4972) (~9–11×).
- **Weak-memory concurrency** — [a publication race in Paimon C++ whose compiler-only
  barrier is silent on x86](https://github.com/apache/paimon-cpp/pull/203).

<!-- contribution-stats:start -->
Selected upstream contributions: 54 merged pull requests across 14 repositories in the Apache, DuckDB and Lance ecosystems.
<!-- contribution-stats:end -->

[Browse merged pull requests →](https://github.com/search?q=is%3Apr+author%3Au70b3+is%3Amerged&type=pullrequests) · [lucian1412@outlook.com](mailto:lucian1412@outlook.com)
