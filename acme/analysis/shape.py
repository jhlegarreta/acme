# -*- coding: utf-8 -*-

from dipy.tracking.metrics import length


def analyze_features(xyz, along=False):

    return length(xyz, along=along)
