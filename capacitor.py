#!/usr/bin/env python3
def main() -> None:
    pass


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt as e1:
        print(e1)
    except Exception as e2:
        print(e2)
