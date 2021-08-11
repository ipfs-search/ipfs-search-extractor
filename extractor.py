import elasticsearch
from elasticsearch.helpers import scan
import json

es = elasticsearch.Elasticsearch('http://10.200.200.3:9200')
es_response = scan(
    es,
    index='ipfs_files_v8',
    query={
        "query": {
            "bool": {
                "should": [
                    {
                        "exists": {
                            "field": "metadata.title" # Ensure non-null
                        }
                    },
                    {
                        "wildcard": {
                            "metadata.title": "?*" # Ensure not empty
                        }
                    }
                ]
            }
        },
        "_source": [
            "metadata.title",
            "references"
        ]
    }
)

for item in es_response:
    _source = item['_source']
    metadata = _source['metadata']

    if 'title' in metadata:
        title = metadata['title'][0]
        assert title
        assert '\t' not in title
        if '\n' in title:
            title = title.replace('\n', ' ')
        title = title.strip()
        if not title:
            continue
        references = _source['references']
        if not references:
            parent_hash = 'null'
        else:
            parent_hash = references[0]['parent_hash']
        print('\t'.join([item['_id'], title, parent_hash]))
        # it seems parent_hash is not so useful for me now, you could also export the json like below🔽 if you like(I will analyse the sites via title):
        # print(json.dumps({'hash': item['_id'], 'title':title}))
