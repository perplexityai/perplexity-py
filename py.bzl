load(
    "@rules_python//python:defs.bzl",
    _py_library = "py_library",
    _py_test = "py_test",
)

def perplexity_py_library(name, imports = [], **kwargs):
    package = native.package_name()
    if package == "src":
        imports = imports + ["."]
    elif package.startswith("src/"):
        imports = imports + ["/".join([".."] * (len(package.split("/")) - 1))]
    elif package == "tests":
        imports = imports + [".."]
    elif package.startswith("tests/"):
        imports = imports + ["/".join([".."] * len(package.split("/")))]

    _py_library(
        name = name,
        imports = imports,
        **kwargs
    )

def bazel_py_test(**kwargs):
    _py_test(**kwargs)

def pytest_test(name, srcs, deps = [], main = None, data = [], **kwargs):
    test_files = [":{}".format(src) for src in srcs]
    runtime_deps = [
        "//src:perplexity",
        "//tests:__init__",
        "//tests:utils",
        "@pip//dirty_equals",
        "@pip//pytest",
        "@pip//pytest_asyncio",
        "@pip//respx",
    ]
    _py_test(
        name = name,
        srcs = ["//:pytest_main.py"],
        main = "//:pytest_main.py",
        args = [
            "-c",
            "$(rootpath //:pyproject.toml)",
        ] + ["$(rootpath {})".format(src) for src in test_files],
        data = data + test_files + [
            "//:README.md",
            "//:pyproject.toml",
        ] + native.glob(["*.txt"], allow_empty = True),
        deps = deps + [dep for dep in runtime_deps if dep not in deps],
        **kwargs
    )
