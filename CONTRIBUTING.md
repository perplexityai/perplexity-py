## Development

Install [Bazelisk](https://github.com/bazelbuild/bazelisk), install development
tools, then enable Git hooks:

```sh
pnpm install --frozen-lockfile
pnpm lefthook install
```

Bazel provisions Python and all Python dependencies. No virtual environment is
required.

## Dependencies and BUILD files

Declare development dependencies in `requirements-dev.in`, then update the
locked requirements:

```sh
bazel run //:requirements.update
```

`gazelle_py` owns test BUILD targets:

```sh
bazel run //:gazelle
```

Commit generated `BUILD.bazel` and `requirements-dev.txt` changes.

## Tests

Run all tests, including source type checking and wheel construction:

```sh
bazel test //...
```

Run one test:

```sh
bazel test //tests:test_client
```

## Linting and formatting

Lefthook runs Gazelle, mypy, and Ruff:

```sh
pnpm lefthook run pre-commit --all-files
```

Apply Ruff fixes:

```sh
bazel run //:ruff -- check --fix .
bazel run //:ruff -- format .
```

## Building

Build the wheel:

```sh
bazel build //:wheel
```

The wheel is written beneath `bazel-bin`.

## Generated code

Most SDK code is generated. Manual changes survive regeneration but may
conflict with later generator output. The generator does not modify
`src/perplexity/lib/` or `examples/`.

## Examples

Run examples with any Python environment containing the built package:

```sh
python examples/<example>.py
```

## Publishing

Release Please creates release PRs and GitHub releases. A published release
triggers the `Publish PyPI` workflow, which builds and publishes `//:wheel`.
The workflow requires `PERPLEXITY_PYPI_TOKEN` or `PYPI_TOKEN`.
