from collections import defaultdict


class ConflictError(Exception):
    pass


def find_manager(
        supervisors, connections, enemies, managers, manager_id, workers_group):

    can_be_manager = []
    for worker in workers_group:
        for supervisor in supervisors[worker]:
            if supervisor in workers_group:
                break
        else:
            can_be_manager.append(worker)

    group_enemies = set()
    for worker in workers_group:
        for enemy in enemies[worker]:
            group_enemies.add(enemy)

    for worker in can_be_manager:
        if worker not in group_enemies:
            manager = worker
            break
    else:
        raise ConflictError()

    managers[manager] = manager_id

    groups = {manager: 0}
    group = 0

    for worker in workers_group:
        if worker == manager:
            continue
        if worker not in groups:
            group += 1
            set_group(workers_group, worker, connections, groups, group)

    workers_groups = defaultdict(list)
    for worker, group in groups.iteritems():
        workers_groups[group].append(worker)

    for group, new_workers_group in workers_groups.iteritems():
        if group == 0:
            continue
        find_manager(
            supervisors, connections, enemies, managers, manager,
            new_workers_group
        )


def set_group(workers_group, worker, connections, groups, group):
    groups[worker] = group
    for connected_workers in connections[worker]:
        if connected_workers in workers_group and \
                connected_workers not in groups:
            set_group(
                workers_group, connected_workers, connections, groups, group)


def reo(workers, relations):

    managers = {}
    workers_group = range(1, workers+1)
    supervisors = defaultdict(list)
    connections = defaultdict(list)
    enemies = defaultdict(list)

    for worker_a, worker_b, value in relations:
        if value == 1:
            supervisors[worker_a].append(worker_b)
            connections[worker_a].append(worker_b)
            connections[worker_b].append(worker_a)
        else:
            enemies[worker_a].append(worker_b)

    try:
        find_manager(
            supervisors, connections, enemies, managers, 0, workers_group)
    except ConflictError:
        return []

    return [managers.get(worker, None) for worker in xrange(1, workers + 1)]