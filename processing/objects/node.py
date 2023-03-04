#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Base
from dataclasses import dataclass, field


@dataclass
class Node:
    id: int

    lat: float
    lon: float

    tags: dict[str] = field(default_factory=list)
