#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Base
from dataclasses import dataclass


@dataclass
class Node:
    id: int

    lat: float
    lon: float
