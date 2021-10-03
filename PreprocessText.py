from gensim.parsing.preprocessing import strip_non_alphanum, strip_multiple_whitespaces, preprocess_string, \
    split_alphanum, strip_short, strip_numeric
import re  # For preprocessing raw text
from pyvi import ViTokenizer  # For split vietnamese words

def rawTextPreprocess(raw):
    # remove link in text
    raw = re.sub(r"http\S+", "", raw)

    # remove characters not belong alphabet
    raw = strip_non_alphanum(raw).lower().strip()

    # split words not meaning
    raw = split_alphanum(raw)

    # remove words alone
    raw = strip_short(raw, minsize=2)

    # remove number in text
    raw = strip_numeric(raw)

    # ghep cac tu tieng viet
    raw = ViTokenizer.tokenize(raw)

    return raw