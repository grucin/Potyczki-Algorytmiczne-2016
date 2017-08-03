import operator


def sze(cores, input_tasks):

    tasks = []
    for task, (p, k, c) in enumerate(input_tasks):
        tasks.append((task, p, k - p - c, c))
    tasks.sort(key=operator.itemgetter(2))

    time = 0
    while True:
        available_cores = cores
        unfinished_tasks = []
        for task, start, reserve, work in tasks:
            if start == time:
                if available_cores > 0:
                    available_cores -= 1
                    if work > 1:
                        unfinished_tasks.append((
                            task, start + 1, reserve, work - 1))
                elif reserve == 0:
                    return 0
                else:
                    unfinished_tasks.append((
                        task, start + 1, reserve - 1, work))
            else:
                unfinished_tasks.append((
                    task, start, reserve, work))

        if not unfinished_tasks:
            break

        tasks = sorted(unfinished_tasks, key=operator.itemgetter(2))
        time += 1

    return 1
