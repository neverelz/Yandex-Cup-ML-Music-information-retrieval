a1 = int(input())
b1 = int(input())
c1 = int(input())
d1 = int(input())

result = []
result1 = []


def results(a, b, c, d):
    def_ = []
    k = 0
    if (a == 0 and c == 0) or (b == 0 and d == 0):
        k = 1
        def_.append(1)
        def_.append(1)
    else:
        if a == 0:
            k = 1
            def_.append(1)
            def_.append(c + 1)
        if b == 0:
            k = 1
            def_.append(1)
            def_.append(d + 1)
        if c == 0:
            k = 1
            def_.append(a + 1)
            def_.append(1)
        if d == 0:
            k = 1
            def_.append(b + 1)
            def_.append(1)

    if k == 0:
        if a + c > b + d:
            if c == d:
                def_.append(1)
                def_.append(d + 1)
            elif a == d and b == c:
                def_.append(max(a, b) + 1)
                def_.append(1)
            else:
                def_.append(b + 1)
                def_.append(d + 1)
        elif a + c < b + d:
            if a == b:
                def_.append(a + 1)
                def_.append(1)
            elif a == d and b == c:
                def_.append(max(a, b) + 1)
                def_.append(1)
            else:
                def_.append(a + 1)
                def_.append(c + 1)
        elif a == b == c == d:
            def_.append(a + 1)
            def_.append(1)
        else:
            if a == b and c == d:
                def_.append(min(a, c) + 1)
                def_.append(1)
            elif a == d and b == c:
                def_.append(max(a, b) + 1)
                def_.append(1)
            else:
                if max(a, c) > max(b, d):
                    def_.append(min(max(a, c), max(b, d)) + 1)
                    def_.append(1)
                else:
                    def_.append(1)
                    def_.append(min(max(a, c), max(b, d)) + 1)
    return def_


if ((min(max(a1, b1), max(c1, d1)) + 2) < sum(results(a1, b1, c1, d1))) and (a1 and b1 and c1 and d1) > 0:
    if max(a1, b1) > max(c1, d1):
        print(1, min(max(a1, b1), max(c1, d1)) + 1)
    else:
        print(min(max(a1, b1), max(c1, d1)) + 1, 1)
else:
    print(results(a1, b1, c1, d1)[0], results(a1, b1, c1, d1)[1])

