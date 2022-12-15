# -*- coding: utf-8 -*-
from collections import namedtuple

Dimensions = namedtuple("Dimensions", ["width", "height"])
Paperparams = namedtuple("Paperparams", ["size", "orientation"])

A0_vertical = Dimensions(841, 1189)
A1_vertical = Dimensions(594, 841)
A2_vertical = Dimensions(420, 594)
A3_vertical = Dimensions(297, 420)
A4_vertical = Dimensions(210, 297)


A0_horizontal = Dimensions(1189, 841)
A1_horizontal = Dimensions(841, 594)
A2_horizontal = Dimensions(594, 420)
A3_horizontal = Dimensions(420, 297)
A4_horizontal = Dimensions(297, 210)

size_dict = {A0_vertical: Paperparams('A0', 'Вертикальный'),
             A1_vertical: Paperparams('A1', 'Вертикальный'),
             A2_vertical: Paperparams('A2', 'Вертикальный'),
             A3_vertical: Paperparams('A3', 'Вертикальный'),
             A4_vertical: Paperparams('A4', 'Вертикальный'),

             A0_horizontal: Paperparams('A0', 'Горизонтальный'),
             A1_horizontal: Paperparams('A1', 'Горизонтальный'),
             A2_horizontal: Paperparams('A2', 'Горизонтальный'),
             A3_horizontal: Paperparams('A3', 'Горизонтальный'),
             A4_horizontal: Paperparams('A4', 'Горизонтальный'),
             }
