# Contributing

## Setup

Install Node 26 and [Bazelisk](https://github.com/bazelbuild/bazelisk), then
enable the repository's pinned `pnpm`:

```sh
npm install --global corepack@latest
corepack enable pnpm
pnpm install --frozen-lockfile
pnpm lefthook install
```

Bazel provisions Python and Python dependencies. No virtual environment is
required.

## Make changes

Handwritten client, transport, and helper code lives under `src/perplexity/`.
Do not edit `src/perplexity/generated/` or `src/perplexity/resources/`; the SDK
code is produced by a private SDK codegen pipeline.

Tests live under `tests/`. Live API tests live under `e2e/live/` and must remain
small and deterministic.

For a dependency change:

1. Update dependencies in `pyproject.toml`. Change `uv.toml` only for UV
   resolver or index configuration.
2. Keep the `py_wheel.requires` metadata in `BUILD.bazel` aligned.
3. Update the lock and BUILD files:

   ```sh
   bazel run //:uv_lock.update
   bazel run //:gazelle
   ```

Commit resulting `uv.lock` and `BUILD.bazel` changes.

Use [Conventional Commits](https://www.conventionalcommits.org/), such as
`fix: handle empty responses` or `feat: add a resource`. Release Please uses
these commits to choose the next version and build the changelog.

## Test

Run the same main test suite as CI:

```sh
bazel test //...
```

Run one target while iterating:

```sh
bazel test //tests:test_client_test
```

Validate formatting, lint, types, and generated BUILD files:

```sh
pnpm lefthook run pre-commit --all-files --force --fail-on-changes
```

Apply Ruff fixes:

```sh
bazel run //:ruff -- check --fix .
bazel run //:ruff -- format .
```

Live tests call the production API and require a token. Run only the relevant
shard:

```sh
PPLX_API_TOKEN=... bazel test //e2e/live:search --test_env=PPLX_API_TOKEN
```

Build the publishable wheel:

```sh
bazel build //:wheel
```

The output is under `bazel-bin/`.

## Release

Do not bump versions or publish from a development branch.

1. Merge normal PRs into `main`.
2. Release Please creates or updates a `release: <version>` PR from Conventional
   Commits.
3. Review and merge that PR. It updates the changelog and version files, then
   creates the `v<version>` tag and GitHub release.
4. The published GitHub release triggers `Publish PyPI`, which runs
   `bazel run //:wheel.publish`.

Release automation requires `RELEASE_TOKEN`. PyPI publishing currently uses
`PERPLEXITY_PYPI_TOKEN`, with `PYPI_TOKEN` as a fallback. For a failed upload,
rerun `Publish PyPI` against the existing release tag; do not create a new
version.
