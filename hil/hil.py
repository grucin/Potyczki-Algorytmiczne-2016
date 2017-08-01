
START_POSITION = (1, 0)
START_VELOCITY = [1, 1]

VERTICAL = (-1, 1)
HORIZONTAL = (1, -1)

BASE_HILL = {
    (1, 2): VERTICAL,
    (2, 3): HORIZONTAL,
    (3, 2): VERTICAL
}


def hil_length_to_point(x, y, n):
    length = 0
    for i in xrange(n-1, -1, -1):
        _x = (x >> i) & 1
        _y = (y >> i) & 1

        if _y == 0:
            tmp = x
            x = y ^ (-_x)
            y = tmp ^ (-_x)

        length = 4 * length + 2 * _x + (_x ^ _y)

    return length


def get_board(n):
    if n == 1:
        return BASE_HILL
    else:
        prev_size = 2 ** n
        prev_board = get_board(n - 1)
        size = 2 ** (n + 1)
        board = {}
        for (x, y), (vx, vy) in prev_board.iteritems():
            # left up:
            board[(x, y + prev_size)] = (vx, vy)
            # right up:
            board[(x + prev_size, y + prev_size)] = (vx, vy)
            # left down:
            board[(y, prev_size - x)] = (-vx, -vy)
            # right down
            board[(2 * prev_size - y, x)] = (-vx, -vy)
            # join
            board[(1, prev_size)] = VERTICAL
            board[(size - 1, prev_size)] = VERTICAL
            board[(prev_size, prev_size + 1)] = HORIZONTAL
    return board


def hil(n, times):
    position = START_POSITION
    velocity = START_VELOCITY
    size = 2 ** (n + 1)
    borders = (0, size)
    results = []
    # board = get_board(n)
    for t in xrange(1, times[-1]+1):
        position = (position[0] + velocity[0], position[1] + velocity[1])
        if t in times:
            results.append(position)
        # if position in board:
        #     x, y = board[position]
        #     velocity = [velocity[0] * x, velocity[1] * y]
        if position[0] in borders:
            velocity[0] = -velocity[0]
        elif position[1] in borders:
            velocity[1] = -velocity[1]
        else:
            # check if on line
            x = position[0] - 1
            y = position[1] - 1
            if x % 2 == 1:
                _v = HORIZONTAL
                a = ((x - 1) / 2, y / 2)
                b = (a[0] + 1, a[1])
            else:
                _v = VERTICAL
                a = (x / 2, (y - 1) / 2)
                b = (a[0], a[1] + 1)

            if abs(
                    hil_length_to_point(a[0], a[1], n)
                    - hil_length_to_point(b[0], b[1], n)) == 1:
                velocity = [velocity[0] * _v[0], velocity[1] * _v[1]]

    return results