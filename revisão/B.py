def call(c: str) -> int:
    return (ord(c) - 65 + (c > "R")) // 3 + 2


if __name__ == "__main__":
    # qtd = int(input())
    # words = [input() for _ in range(qtd)]
    words = ["PORTOSEGURO", "FATEC", "TECNOLOGIA"]

    for word in words:
        print("".join(str(call(c)) for c in word))
