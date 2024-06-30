import calc

def main():
    test_square()

def test_square():
    try:
        assert calc.square(2) == 4
    except AssertionError:
        print("2 squared wasnt 4")
    try:
        assert calc.square(3) == 9
    except AssertionError:
        print("3 squared was not 9")

if __name__ == "__main__":
    main()