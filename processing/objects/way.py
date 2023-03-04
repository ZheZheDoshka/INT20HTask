#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Base
from dataclasses import dataclass, field

# Internal
from processing.objects.node import Node


@dataclass
class Way:
    id: int

    nodes: list[Node]

    tags: dict[str] = field(default_factory=list)
