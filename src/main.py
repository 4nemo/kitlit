class Story:
    """Story object definition"""

    def __init__(
        self,
        title: str = None,
        description: str = None,
    ):
        self.title = title
        self.description = description


def main():
    print("Hello from kitlit!")


if __name__ == "__main__":
    main()
