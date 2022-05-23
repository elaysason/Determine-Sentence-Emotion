##from _future_ import unicode_literals, print_function, division
from io import open
import unicodedata
import string
import re
import random
import numpy as np
import torch
import torch.nn as nn
from torch import optim
import torch.nn.functional as F
import pandas as pd

def unicodeToAscii(s):
    return ''.join(
        c for c in unicodedata.normalize('NFD', s)
        if unicodedata.category(c) != 'Mn'
    )

# Lowercase, trim, and remove non-letter characters


def normalizeString(s):
    s = unicodeToAscii(s.lower().strip())
    s = re.sub(r"([.!?])", r" \1", s)
    s = re.sub(r"[^a-zA-Z.!?]+", r" ", s)
    return s

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
train = pd.io.parsers.read_csv("trainEmotions.csv")
train_data = torch.tensor(train['content'].values)
train_labels = torch.tensor(train['emotion'].values)