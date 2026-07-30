# Agent guidance

Follow [CONTRIBUTING.md](./CONTRIBUTING.md) for setup, development, and release
commands.

## Scope

- Treat `src/perplexity/generated/` and `src/perplexity/resources/` as output
  from a private SDK codegen pipeline. Do not edit them.
- Keep handwritten changes focused and preserve unrelated generated files.
- Declare dependencies in `pyproject.toml`; use `uv.toml` only for UV resolver
  or index configuration. Keep `BUILD.bazel` wheel metadata aligned.

## Workflow

- Use Bazel targets instead of direct Python test or build commands.
- Run `bazel run //:uv_lock.update` after dependency changes.
- Run `bazel run //:gazelle` after adding files or changing imports.
- Do not bump versions, edit release PR output, or publish packages manually.

## Validation

- Run `bazel test //...`.
- Run `pnpm lefthook run pre-commit --all-files --force --fail-on-changes`.
- Run live tests only when explicitly requested and `PPLX_API_TOKEN` is
  available.
