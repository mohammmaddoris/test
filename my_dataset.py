# coding=utf-8

import numpy as np
from torch.utils.data import Dataset

class My_Dataset(Dataset):
    def __init__(self, contaX, ddeltaX, begin, length):
        super(My_Dataset, self).__init__()

        self.contaX = contaX
        self.ddeltaX = ddeltaX

        self.begin = begin
        self.length = length

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        return {"Point": self.contaX[self.begin + index], "Delta": self.ddeltaX[self.begin + index]}