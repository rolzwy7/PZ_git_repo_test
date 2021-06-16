import argparse

parser = argparse.ArgumentParser()


def bob():
    print("Bob")
    return "bob"


def anna():
    print("Anna")
    return 1


def main():
    print("Bob")
    print("Bob2")


if __name__ == "__main__":
    main()
