def rule_schedule(start, stop, div):
    def wrapper(min):
        if stop > start:
            return start <= min % div < stop
        else:
            return min % div < start or min % div >= stop

    return wrapper


def ping(host1, host2, rule, min):
    out = host1.cmd('ping -c 1 %s' % host2.IP())
    index = out.find('received')
    ret = out[index - 2]
    if rule(min):
        return ret == '1'
    else:
        return ret == '0'