def camel_case_split(s):
    """https://stackoverflow.com/a/58996565"""
    idx = list(map(str.isupper, s))
    # mark change of case
    l = [0]
    for (i, (x, y)) in enumerate(zip(idx, idx[1:])):
        if x and not y:  # "Ul"
            l.append(i)
        elif not x and y:  # "lU"
            l.append(i + 1)
    l.append(len(s))
    # for "lUl", index of "U" will pop twice, have to filter that
    return [s[x:y] for x, y in zip(l, l[1:]) if x < y]


def split_camelcase_to_underscore(text):
    return "_".join(camel_case_split(text))


def remove_underscore(string, index):
    return string.split("_")[index]


def get_channel(checkbox):
    channel = int(remove_underscore(str(checkbox.objectName()), 1))

    return channel


# def get_key(checkbox):
#     """
#     This returns a key string in python naming convention with underscores and converts from the Qt object name in
#     camel case
#
#     Args: checkbox: QtCheckbox widget
#
#     Returns: key string
#
#     """
#
#     key = remove_underscore(str(checkbox.objectName()), 0)
#
#     return split_camelcase_to_underscore(key)


def get_key(checkbox):
    """
    This returns a key string in python naming convention with underscores and converts from the Qt object name in
    camel case

    Args: checkbox: QtCheckbox widget

    Returns: key string

    """

    key_lookup = {"enableDAC": "enable",
                  "signBit": "sign_bit"}

    return key_lookup[str(checkbox.objectName())]