#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

from acme.analysis.shape import analyze_features


def test_analyze_features():

    xyz = np.array([[1, 1, 1], [2, 3, 4], [0, 0, 0]])
    expected_lens = np.sqrt([1 + 2**2 + 3**2, 2**2 + 3**2 + 4**2])
    assert analyze_features(xyz) == expected_lens.sum()

