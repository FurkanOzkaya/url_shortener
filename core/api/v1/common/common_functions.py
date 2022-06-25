BASE = 62
CHARSET_DEFAULT = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

string_types = (str,)


def id_to_short_url(id, minlength=1, charset=CHARSET_DEFAULT):
    """
        ID to short url
        @params:
        id  unique number
        minlength=1  length of short url
        charset=CHARSET_DEFAULT char set for base62
    """

    short_url = []
    while(id > 0):
        short_url += CHARSET_DEFAULT[id % 62]
        id //= 62

    if len(short_url) > 0:
        short_url.reverse()
    else:
        short_url.append("0")

    short_url = "".join(short_url)
    short_url = charset[0] * max(minlength - len(short_url), 0) + short_url
    return short_url


def short_url_to_id(encoded, charset=CHARSET_DEFAULT):
    length = len(encoded)
    res_id = 0

    for i, x in enumerate(encoded):
        res_id += _value(x, charset=charset) * (BASE ** (length - (i + 1)))

    return res_id


def _value(ch, charset):
    """Decodes an individual digit of a base62 encoded string."""

    try:
        return charset.index(ch)
    except ValueError:
        raise ValueError("base62: Invalid character (%s)" % ch)
