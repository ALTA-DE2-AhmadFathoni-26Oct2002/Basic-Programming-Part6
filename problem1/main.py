def compare(a, b):
    pattern = ""
    huruf = min(len(a), len(b))

    for x in range (huruf):
            if a[x] == b[x]:
                pattern += a[x]
            else:
                break

    return pattern

if __name__ == '__main__':
    print(compare("AKA", "AKASHI")) # AKA
    print(compare("KANGOORO", "KANG")) # KANG
    print(compare("KI", "KIJANG")) # KI
    print(compare("KUPU-KUPU", "KUPU")) # KUPU
    print(compare("ILALANG", "ILA")) # ILA