"""
This script implements data inserting
"""
import json
from elasticsearch import Elasticsearch
from elasticsearch import helpers
from const import (
    WORDS_DIR,
    ES_HOST,
    ES_PORT
)

es = Elasticsearch(host= ES_HOST, port= ES_PORT)
es = Elasticsearch()


def load_word_data():
    with open(WORDS_DIR) as f:
        wiki_words = f.read().split("\n")[:-1]
    return wiki_words


# there is some problems if multi types and doc type exist simultaneously
def create_index_and_set_mapping(index):
    request_body = {
	    "settings" : {
	        "number_of_shards": 5,
	        "number_of_replicas": 1
	    },
	    #"mappings": {
        #    "properties": {
        #        "word": {"type": "text", "index": True},
        #        "importance": {"type": "boolean", "index": False}
        #    }
        #}
    }
    es.indices.create(index=index, body=request_body)


def generate_bulk_actions(_index, _type, wiki_data):
    bulk_actions = [
        {
            "_index": _index,
            "_type": _type,
            "_id": i,
            "_source": {
                "word": d,
                "importance": True if " " in d else False
            }
        }
        for i, d in enumerate(wiki_data)
    ]
    return bulk_actions


def insert_data_by_bulk(actions):
    res = helpers.bulk(es, actions)


if __name__ == "__main__":
    index = "wiki_prefix_search"
    _type = "wiki_word_lst"
    create_index_and_set_mapping(index)
    wiki_words = load_word_data()
    bulk_actions = generate_bulk_actions(index, _type, wiki_words)
    insert_data_by_bulk(bulk_actions)
