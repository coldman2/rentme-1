import datetime
import re


def reduce_mapping(to_convert, name_mapping=None, keep_list=None, ignore_keys=None):
    mapping = {}
    if name_mapping is not None:
        mapping.update(name_mapping)
    if keep_list is not None:
        mapping.update(zip(keep_list, keep_list))
    if not mapping:
        raise ValueError('No mappings supplied. Assuming this is a bug')
    assert len(mapping) == len(set(mapping.values())), 'Not 1-to-1'
    if ignore_keys is not None:
        mapping.update(dict.fromkeys(ignore_keys, False))
    new_dictionary = {}
    skipped_keys = []
    for key, value in to_convert.items():
        new_key = mapping.get(key, None)
        if new_key:
            new_dictionary[new_key] = value
        elif new_key is None:
            skipped_keys.append(key)
    if skipped_keys:
        raise ValueError("Reduce Mapping skipped the following keys %r" % (skipped_keys,))
    return new_dictionary


def title_to_snake_case_mapping(*args, extra=None, extras=None, prefix=''):
    name_mapping = {}
    for old_name in args:
        assert re.fullmatch(r'([A-Z]+[^A-Z ]*)+', old_name), \
               'String must be title case'
        words = re.findall(r'[A-Z]+[^A-Z]*', old_name)
        new_name = '_'.join(map(str.lower, words))
        name_mapping[old_name] = prefix + new_name
    if extra is not None:
        name_mapping.update(extra)
    if extras is not None:
        name_mapping.update(*extras)
    # Assert there is a 1-to-1 mapping between old and new names.
    assert len(name_mapping) == len(set(name_mapping.values()))
    return name_mapping


def date_convert(date_string):
    if not date_string:
        return None
    match = re.fullmatch(r'/Date\(([1-9][0-9]*|0)\)/', date_string)
    if match:
        utc_unix_seconds = int(match.group(1)) / 1000
        return datetime.datetime.fromtimestamp(utc_unix_seconds,
                                               tz=datetime.timezone.utc)
    else:
        raise ValueError('The given date string(%r) is not in a supported'
                         ' format' % (date_string, ))


def date_convert_many(object, *keys_to_convert):
    for key in keys_to_convert:
        if key in object:
            object[key] = date_convert(object[key])
    return object


def enum_convert_many(object, keys_to_enum_mapping):
    for key, enum_cls in dict(keys_to_enum_mapping).items():
        if key in object:
            try:
                object[key] = enum_cls(object[key])
            except:
                object[key] = enum_cls.__members__[object[key]]
    return object
