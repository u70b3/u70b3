# Hi, I'm Kid 👋

I'm an open-source data systems contributor working at the hard boundaries between
query engines, lakehouse formats, and index infrastructure. I turn correctness,
durability, compatibility, and performance problems into tested upstream changes.

- **Correctness and durability:** WAL generations and fencing, cache/object-store
  lifetimes, weak-memory concurrency, safe FFI boundaries, overflow and NULL semantics,
  and failure propagation.
- **Query and index behavior:** SQL compatibility, Parquet pruning, HNSW/IVF algorithm
  alignment, and vectorized Arrow execution.
- **Lakehouse interoperability:** Iceberg/Paimon/DuckLake metadata, time travel,
  delete and rewrite paths, plus safe cross-language APIs.

I mostly work in **Rust and C++**, following problems into Java, Python, Node.js, or C
when the boundary requires it. I favor explicit invariants, compatibility-preserving
changes, reproducible failures, and benchmarks that explain—not merely report—performance.

Contributions include **Lance/LanceDB**, **DuckDB/DuckLake**, and Apache projects
such as **Doris, DataFusion/Comet, Iceberg, and Paimon**.

## Selected contributions

- [Expose Lance indexes through `SHOW INDEX` in Apache Doris](https://github.com/apache/doris/pull/66637)
- [Add distributed index segment build APIs to Lance C](https://github.com/lance-format/lance-c/pull/57)
- [Harden DuckDB's ARM64 portability and undefined behavior](https://github.com/duckdb/duckdb/pull/24884)
- [Fix watermark binary searches with null watermarks in Apache Paimon](https://github.com/apache/paimon/pull/9037)
- [Vectorize `spark_unscaled_value` in Apache DataFusion Comet](https://github.com/apache/datafusion-comet/pull/4972)

<!-- contribution-stats:start -->
Selected upstream contributions: 47 merged pull requests across 14 repositories.
<!-- contribution-stats:end -->

[Browse all my pull requests →](https://github.com/search?q=is%3Apr+author%3Au70b3&type=pullrequests)
