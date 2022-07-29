def hello_world(name: str) -> str:
    return f"hello, {name}."


if __name__ == "__main__":
    greeting = hello_world("bob")
    print(greeting)
