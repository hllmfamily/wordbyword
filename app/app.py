import typefx.typefx as _typefx

def main():
    """Print out results
    """
    LINES = [
        'A B C DEF GHL . JALSJDKJL AJS',
        'b B C DEF GHL . JALSJDKJL AJS',
        'c B C DEF GHL . JALSJDKJL AJS',
        'd B C DEF GHL . JALSJDKJL AJS'
    ]

    for line in LINES:
        _typefx.dynamic(line)
        print('\n')


if __name__ == "__main__":
    main()
    print('END OF GAME')