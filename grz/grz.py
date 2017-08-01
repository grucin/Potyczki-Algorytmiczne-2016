import operator


def grz(glade_description):
    glades = len(glade_description)
    selected = set()
    result = []
    for day in xrange(glades):
        counts = [
            (glade, start_value + day * increment)
            for glade, (increment, start_value) in enumerate(glade_description)]
        counts.sort(key=operator.itemgetter(1), reverse=True)
        for glade, _ in counts:
            if glade not in selected:
                selected.add(glade)
                break
        selected_order = [
            (glade, glade_description[glade][0])
            for glade in selected
        ]
        selected_order.sort(key=operator.itemgetter(1))
        value = 0
        for _day, (glade, increment) in enumerate(selected_order):
            value += glade_description[glade][1] + _day * increment
        result.append(value)

    return result