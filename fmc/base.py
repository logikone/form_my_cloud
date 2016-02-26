import json
import collections

class Base(object):
    def __init__(self):
        pass

    def serialize(self, doc):
        return json.dumps(
                doc,
                sort_keys=True,
                indent=4,
                separators=(",", ":"),
                )

    def _update_dict(self, d, u):
        for k, v in u.iteritems():
            if isinstance(v, collections.Mapping):
                r = self._update_dict(d.get(k, {}), v)
                d[k] = r
            else:
                d[k] = u[k]
        return d

#! vim: ts=4 sw=4 ft=python expandtab:
