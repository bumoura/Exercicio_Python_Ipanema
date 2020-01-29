# -*- coding: utf-8 -*-

palavra = ('')
with open('musica.txt') as f:   
  ocorrencias = f.read().count(palavra)
print(ocorrencias)

from collections import Counter

with open('musica.txt') as f:
    ocorrencias = Counter(f.read().upper().split())
print(ocorrencias)  






