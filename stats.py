import re

def get_word_count(text):
    return len(list(filter(lambda x: x != '', re.split(r'\s+', text))))


def get_character_count(text):
    count_dict = {}
    for t in text:
        next_char = t.lower()
        if next_char not in count_dict.keys():
            count_dict[next_char] = 1
        else:
            count_dict[next_char] += 1

    return count_dict


def make_sorted_dict(dictionary):
    itemized = [{'char': k, 'count': v} for k, v in dictionary.items() if ord(k) > 32]
    return sorted(itemized, key=lambda x: x['count'], reverse=True)
