from collections import Counter, defaultdict
import sys
import re

# ==============================================================================
# name: dna.py
# aim: Functions to process DNA/RNA base pairs from a formatted file.
#
# Written by: Jiaming Yang (z5452842)
# For COMP2041/9044 Lab 10
# ==============================================================================

def read_dna(dna_file):
    """
    Reads base pairs from the given file in the format:
        A <-> T
        G <-> C
    - Accepts optional surrounding whitespace
    - Allows either side to be missing
    - Skips invalid lines
    Returns: list of (base1, base2) tuples
    """
    data = []
    # Allow empty or A/T/G/C/U on either side of <->, ignoring surrounding spaces
    pattern = re.compile(r'^([ATGCU]?)\s*<->\s*([ATGCU]?)$')

    with open(dna_file) as f:
        for line in f:
            line = line.strip()
            match = pattern.match(line)
            if match:
                base1, base2 = match.group(1), match.group(2)
                data.append((base1, base2))
    return data


def is_rna(dna):
    """
    Determines if the base list corresponds to DNA, RNA, or Invalid.
    - DNA if ≥90% of non-empty bases are A/T/G/C
    - RNA if ≥90% are A/U/G/C
    - Otherwise Invalid
    """
    c = Counter()
    for pair in dna:
        c[pair[0]] += 1
        c[pair[1]] += 1

    total = sum(c.values()) - c['']  # exclude missing bases

    if c['A'] + c['T'] + c['G'] + c['C'] >= total * 0.9:
        return "DNA"
    if c['A'] + c['U'] + c['G'] + c['C'] >= total * 0.9:
        return "RNA"
    return "Invalid"


def clean_dna(dna):
    """
    Fills in missing bases using the pairing rules:
    - DNA: A<->T, G<->C
    - RNA: A<->U, G<->C
    - Skips completely empty or invalid pairs
    Returns: list of complete, valid base pairs
    """
    type = is_rna(dna)
    if type == "DNA":
        pairs = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G', '': ''}
    elif type == "RNA":
        pairs = {'A': 'U', 'U': 'A', 'G': 'C', 'C': 'G', '': ''}
    else:
        return []

    new_dna = []
    for pair in dna:
        if pair[0] not in pairs or pair[1] not in pairs:
            continue
        if pair[0] == '' and pair[1] == '':
            continue
        elif pair[0] == '':
            new_dna.append((pairs[pair[1]], pair[1]))
        elif pair[1] == '':
            new_dna.append((pair[0], pairs[pair[0]]))
        else:
            new_dna.append(pair)

    return new_dna


def mast_common_base(dna):
    """
    Returns the most common first base in all pairs.
    (Function name must be mistyped as per test_dna.py)
    """
    c = Counter()
    for pair in dna:
        c[pair[0]] += 1

    if not c:
        return ""  # Could also return "Unknown"
    return c.most_common(1)[0][0]


def base_to_name(base):
    """
    Converts single-letter base to its full chemical name.
    Defaults to 'Unknown' for unrecognized bases.
    """
    name = defaultdict(lambda: "Unknown")
    name.update({
        'A': "Adenine",
        'T': "Thymine",
        'G': "Guanine",
        'C': "Cytosine",
        'U': "Uracil"
    })
    return name[base]