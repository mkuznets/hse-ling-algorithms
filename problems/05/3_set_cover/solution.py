def set_cover(universe, sets):
    result = []
    universe = universe.copy()

    for s in sets:
        top = max(sets, key=lambda x: len(x & universe))

        if not top & universe:
            return []

        universe -= top
        result.append(top)

        if not universe:
            break

    return result


def __set_cover__(universe, sets):
    old_universe = set(universe)
    answer_sets = []
    covered = set()

    while covered != old_universe:
        to_sort = []

        for set_item in sets:
            to_sort.append((len(universe.intersection(set_item)), set_item))

        to_sort = sorted(to_sort)

        answer_sets.append(to_sort[-1][1])

        covered = covered.union(answer_sets[-1])
        universe = universe.difference(answer_sets[-1])
        sets.remove(answer_sets[-1])

    return answer_sets


__set_cover__({1, 2, 3, 4, 5}, [{1, 2, 3, 4}, {1, 2, 3, 4}, {5}])