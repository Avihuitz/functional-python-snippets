import random
def coding():

    flag_words = None
    shift = None
    flag_letters = None
    mapping = {}

    def set_key(s,flag_word,flag_letter):
        nonlocal shift,flag_letters, flag_words
        flag_words = flag_word
        flag_letters = flag_letter

        if s == 0:
            shift = random.randint(1, 26)
            shift = shift if random.choice([True, False]) else -shift
            return 'done'
        else:
            shift = s
            return 'done'

    def empty_key():
        nonlocal shift, flag_words, flag_letters
        shift = None
        flag_words = None
        flag_letters = None
        return 'done'

    def export_key():
        if shift is None:
            return 'key empty'
        key_dict = {}
        flag_l = flag_letters == "yes"
        flag_w = flag_words == "yes"
        if flag_l:
            for i in range(26):
                letter = chr(ord('a') + i)
                shifted_index = (i + shift) % 26
                shifted_letter = chr(ord('a') + shifted_index)
                key_dict[letter] = shifted_letter
        key_dict['reverse_word'] = flag_w
        key_dict['reverse_string'] = flag_l
        return key_dict

    def import_key(key):
        nonlocal flag_words, flag_letters, shift, mapping
        if 'reverse_word' not in key or 'reverse_string' not in key:
            return 'invalid key'
        flag_words = "yes" if key['reverse_word'] else "no"
        flag_letters = "yes" if key['reverse_string'] else "no"
        mapping = {k: v for k, v in key.items() if len(k) == 1 and k.islower()}
        shift = None
        return 'done'

    def encoding(sentence):
        nonlocal shift, flag_letters, flag_words

        if shift is None:
            return "can't encode without shift"
        key = export_key()
        split_s = sentence.split()
        shifted = ""

        if flag_words == "yes":
            split_s = split_s[::-1]

        for i in range(len(split_s)):
            word = split_s[i]

            if flag_letters == "yes":
                word = word[::-1]

            for j in range(len(word)):
                shifted += key.get(word[j], word[j])
            shifted += " "
        return shifted.strip()

    def decoding(sentence):
        nonlocal mapping

        if not mapping:
            if shift is None:
                return 'key empty'
            mapping = {
                chr(ord('a') + i): chr(ord('a') + ((i + shift) % 26))
                for i in range(26)
            }
        reverse_key = {v: k for k, v in mapping.items()}
        split_s = sentence.split()
        shifted = ""

        if flag_words == "yes":
            split_s = split_s[::-1]

        for i in range(len(split_s)):
            word = split_s[i]
            if flag_letters == "yes":
                word = word[::-1]
            for j in range(len(word)):
                shifted += reverse_key.get(word[j], word[j])
            shifted += " "
        return shifted.strip()

    def dispatch(msg, value=None):
        if msg == 'set_key': return set_key(*value)
        elif msg == 'empty_key': return empty_key()
        elif msg == 'export_key': return export_key()
        elif msg == 'import_key': return import_key(value)
        elif msg == 'encoding': return encoding(value)
        elif msg == 'decoding': return decoding(value)
        else: return 'unknown command'
    return dispatch