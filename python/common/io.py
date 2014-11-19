import cPickle
import codecs


def pickle(data, file_path):
    with open(file_path, 'wb') as f:
        cPickle.dump(data, f, cPickle.HIGHEST_PROTOCOL)


def unpickle(file_path):
    with open(file_path, 'rb') as f:
        data = cPickle.load(f)
    return data


def read_list(file_path, coding=None):
    if coding is None:
        with open(file_path, 'r') as f:
            arr = [line.strip() for line in f.readlines()]
    else:
        with codecs.open(file_path, 'r', coding) as f:
            arr = [line.strip() for line in f.readlines()]
    return arr


def write_list(arr, file_path, coding=None):
    if coding is None:
        with open(file_path, 'w') as f:
            f.write('\n'.join(arr))
    else:
        with codecs.open(file_path, 'w', coding) as f:
            f.write(u'\n'.join(arr))


def read_kv(file_path, coding=None):
    if coding is None:
        with open(file_path, 'r') as f:
            dic = {}
            for line in f.readlines():
                k, v = line.strip().split(' ', 1)
                dic[k] = v
    else:
        with codecs.open(file_path, 'r', coding) as f:
            dic = {}
            for line in f.readlines():
                k, v = line.strip().split(' ', 1)
                dic[k] = v
    return dic


def write_kv(dic, file_path, coding=None):
    if coding is None:
        with open(file_path, 'w') as f:
            for k, v in dic.iteritems():
                f.write(k + ' ' + v + '\n')
    else:
        with codecs.open(file_path, 'w', coding) as f:
            for k, v in dic.iteritems():
                f.write(k + u' ' + v + u'\n')
