from __future__ import annotations

import re
import warnings

import numpy as np


class Rng:
    def __init__(self, seed=42):
        self._seed = seed
        self._rng = None

    @property
    def rng(self):
        if self._rng is None:
            self._rng = np.random.default_rng(seed=self._seed)
        return self._rng

    @property
    def seed(self) -> int:
        return self._seed

    @seed.setter
    def seed(self, new_seed: int):
        self._seed = new_seed
        self._rng = None  # Invalidate the existing RNG, forcing lazy re-creation with the new seed

    def choice(self, *args, **kwargs):
        return self.rng.choice(*args, **kwargs)


rng = Rng()  # compatibility


def load_as_score(text):
    """
    validate and returns given text as score
    """

    pattern = r"^[\d.]+$"
    if not re.match(pattern, text):
        warnings.warn("Invalid score")
        score = 0.0
    else:
        score = eval(text)

    return score
