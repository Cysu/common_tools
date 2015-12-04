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
        arr = ['{}'.format(item) for item in arr]
        with open(file_path, 'w') as f:
            f.write('\n'.join(arr))
    else:
        with codecs.open(file_path, 'w', coding) as f:
            f.write(u'\n'.join(arr))


def read_kv(file_path, coding=None):
    if coding is None:
        with open(file_path, 'r') as f:
            key_list = []
            value_list = []
            for line in f.readlines():
                k, v = line.strip().split(' ', 1)
                key_list.append(k)
                value_list.append(v)
    else:
        with codecs.open(file_path, 'r', coding) as f:
            key_list = []
            value_list = []
            for line in f.readlines():
                k, v = line.strip().split(' ', 1)
                key_list.append(k)
                value_list.append(v)
    return key_list, value_list


def write_kv(inp, file_path, coding=None):
    if coding is None:
        with open(file_path, 'w') as f:
            if isinstance(inp, dict):
                for k, v in inp.iteritems():
                    f.write('{} {}\n'.format(k, v))
            elif isinstance(inp, tuple) and len(inp) == 2:
                for k, v in zip(*inp):
                    f.write('{} {}\n'.format(k, v))
            elif isinstance(inp, list):
                for k, v in inp:
                    f.write('{} {}\n'.format(k, v))
            else:
                raise ValueError("Invalid input data type. Should be a "
                                 "dict or a tuple of (key_list, value_list) or "
                                 "a list of [(key, value), ...]")
    else:
        with codecs.open(file_path, 'w', coding) as f:
            if isinstance(inp, dict):
                for k, v in inp.iteritems():
                    f.write(u'{} {}\n'.format(k, v))
            elif isinstance(inp, tuple) and len(inp) == 2:
                for k, v in zip(*inp):
                    f.write(u'{} {}\n'.format(k, v))
            elif isinstance(inp, list):
                for k, v in inp:
                    f.write(u'{} {}\n'.format(k, v))
            else:
                raise ValueError("Invalid input data type. Should be a "
                                 "dict or a tuple of (key_list, value_list) or "
                                 "a list of [(key, value), ...]")