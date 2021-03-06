# -*- coding: utf-8 -*-
"""encoder.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1X2EYuyogFndImO5bPH1cS7IvvwlE3C0-
"""

import torch
import torch.nn as nn

class Encoder(nn.module):
  def __init__(self):
    super().__init__()

    self.emgedding = nn.Embedding()
    pos_table = torch.FloatTensor(get_sinusoid_encoding_table(word_sequence, hight))
    self.position_embedding = nn.Embedding.from_pretrained(pos_table, freeze=True)
    self.att_layers = nn.ModuleList([EncoderLayer() for _ in range(6)])

  def forward(self,inputs, att_mask):
    
    emd_inputs = self.emnedding(inputs) + self.pos_embedding(positions)
    att_probs = []
    for layer in self.att_layers:
      outputs = layer(emd_inputs, att_mask)
      att_probs.append(outputs['att_probs'])

    return {'outputs': outputs['output'], 'att_probs': att_probs}