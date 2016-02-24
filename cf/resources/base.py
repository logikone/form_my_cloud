import json

class ResourceBase(object):
    def serialize(doc):
        return json.dumps(
                doc,
                sort_keys=True,
                indent=4,
                separators=(",", ":"),
                )
