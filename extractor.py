import elasticsearch
from elasticsearch.helpers import scan
import json
import sys
import time

ELASTICSEARCH_URL = 'http://10.200.200.3:9200'
MAX_DOCS = 1024*1024
START_DATE = "2018-01-01T00:00:00Z"
END_DATE = "2019-01-01T00:00:00Z"

es = elasticsearch.Elasticsearch(ELASTICSEARCH_URL)
es_response = scan(
    es,
    index='ipfs_files_v8',
    query={
        "query": {
            "bool": {
                "must": [
                    {
                        "exists": {
                            "field": "metadata.title" # Ensure non-null
                        }
                    },
                    {
                        "wildcard": {
                            "metadata.title": "?*" # Ensure not empty
                        }
                    },
                    {
                        "range": {
                            "first-seen": {
                                "gt": START_DATE,
                                "lte": END_DATE
                            }
                        }
                    }
                ]
            },
        },
        "sort":[
            {
                "first-seen": { # Allows for incremental exports
                    "order": "asc"
                }
            }
        ],
        "_source": [
            "metadata.title",
            "first-seen"
        ]
    },
    preserve_order=True
)

doc_count = 0
start_time = time.time()
first_item = None
last_item = None

for item in es_response:
    _source = item['_source']
    metadata = _source['metadata']

    title = metadata['title'][0]
    title = title.strip()

    # parent_hashes = []
    # for reference in _source['references']:
    #     parent_hashes.append(reference['parent_hash'])
    # references =
    # if not references:
    #     parent_hashes = None
    # else:
    #     parent_hash = references[0]['parent_hash']

    assert _source['first-seen']
    first_seen = _source['first-seen']
    print(json.dumps([item['_id'], title, first_seen]))

    doc_count += 1

    if doc_count == 1:
        first_item = first_seen

    if doc_count == MAX_DOCS:
        break

last_item = first_seen

time_spent = time.time() - start_time
print("{0} documents written in {1}".format(doc_count, time_spent), file=sys.stderr)
print("First item: {0}\nLast item: {1}".format(first_item, last_item), file=sys.stderr)
