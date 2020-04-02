"""
Default Dict Implementation.
"""

# pylint: disable=C0103
class defaultdict:
    """
    Default Dict Implementation.

    Defaultdcit that returns the key if the key is not found in dictionnary (see
    unswap in karma-lib):
    >>> d = defaultdict(default=lambda key: key)
    >>> d['foo'] = 'bar'
    >>> d['foo']
    'bar'
    >>> d['baz']
    'baz'
    DefaultDict that returns an empty string if the key is not found (see
    prefix in karma-lib for typical usage):
    >>> d = defaultdict(default=lambda key: '')
    >>> d['foo'] = 'bar'
    >>> d['foo']
    'bar'
    >>> d['baz']
    ''
    Representation of a default dict:
    >>> defaultdict([('foo', 'bar')])
    defaultdict(None, {'foo': 'bar'})
    """

    @staticmethod
    # pylint: disable=W0613
    def __new__(cls, default_factory=None, **kwargs):
        # Some code (e.g. urllib.urlparse) expects that basic defaultdict
        # functionality will be available to subclasses without them
        # calling __init__().
        self = super(defaultdict, cls).__new__(cls)
        # pylint: disable=C0103
        self.d = {}
        return self

    def __init__(self, default_factory=None, **kwargs):
        self.d = kwargs
        self.default_factory = default_factory

    def __getitem__(self, key):
        try:
            return self.d[key]
        except KeyError:
            val = self.__missing__(key)
            self.d[key] = val
            return val

    def __setitem__(self, key, val):
        self.d[key] = val

    def __delitem__(self, key):
        del self.d[key]

    def __contains__(self, key):
        return key in self.d

    def __missing__(self, key):
        if self.default_factory is None:
            raise KeyError(key)
        return self.default_factory()
