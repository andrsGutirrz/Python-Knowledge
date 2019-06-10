def todo(f, *messages):
    print(f"\n*** TO DO: MUST IMPLEMENT '{f.__name__}' ***")
    for n, message in enumerate(messages):
        print(f"DETAIL # {n} --> {message} <--")
        print()
    return f