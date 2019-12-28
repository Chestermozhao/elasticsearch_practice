"""
This script implements transfering raw data to bulk data
Author: Chestermo
Email: b02310043@gmail.com
Date: 2019-12
"""
import os
import json
from const import WORD_LST_DIR


def load_word_data():
    with open(WORD_LST_DIR) as f:
        wiki_words = f.read().split("\n")[:-1]
    return wiki_words


def prepare_bulk_insert_data(raw_data, filename, index):
    dir_path = os.path.dirname(__file__)
    file_path = os.path.join(dir_path, "data", filename)
    with open(file_path, "w") as f:
        for i, d in enumerate(raw_data):
            index_info = {"index": {"_index": index, "_id": i}}
            json.dump(index_info, f)
            f.write("\n")
            is_important = True if " " in d else False
            wiki_word_d = {"word": d, "importance": is_important}
            json.dump(wiki_word_d, f)
            f.write("\n")


if __name__ == "__main__":
    index = "wiki_prefix_search"
    filename = "wiki_words.json"
    wiki_words = load_word_data()
    prepare_bulk_insert_data(wiki_words, filename, index)
