def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # rule 1: length
    if not (2 <= len(s) <= 6):
        return False

    # rule 2: first two chars letters
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    # rule 3: only alphanumeric
    if not s.isalnum():
        return False

    # rules 4 & 5: digit rules
    for i, ch in enumerate(s):
        if ch.isdigit():
            if ch == "0":
                return False
            if not s[i:].isdigit():
                return False
            break

    return True


main()
