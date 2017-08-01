
def sum_jed(n):
    return '+'.join('1' for _ in xrange(n))


def jed_count(expr):
    return len(expr.split('1')) - 1


def _jed(n):
    for i in xrange(2, n):
        if n % i == 0:
            return '({})*({})'.format(_jed(i), _jed(n / i))
    else:
        if n > 3:
            return '1+{}'.format(_jed(n - 1))
    return sum_jed(n)


def jed(n):
    expr = _jed(n)
    if jed_count(expr) > 100:
        return 'NIE'
    return expr