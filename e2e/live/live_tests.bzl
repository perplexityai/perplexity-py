load("//:py.bzl", "pytest_test")

def live_tests():
    for name in [
        "async_chat_completion",
        "chat_completion",
        "contextualized_embeddings",
        "embeddings",
        "responses",
        "search",
        "streaming_chat",
        "streaming_responses",
    ]:
        pytest_test(
            name = name,
            timeout = "long" if name == "async_chat_completion" else "moderate",
            srcs = ["test_{}.py".format(name)],
            tags = [
                "functional_test",
                "manual",
            ],
            deps = [":helpers"],
        )
