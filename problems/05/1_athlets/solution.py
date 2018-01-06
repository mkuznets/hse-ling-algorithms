def tower(athlets):
    if not athlets:
        return 0, []

    athlets = sorted(athlets, key=lambda x: x[1])
    acc = 0
    n = 0

    for i, (m, s) in enumerate(athlets):
        if s < acc:
            continue
        acc += m
        n += 1

    return n
