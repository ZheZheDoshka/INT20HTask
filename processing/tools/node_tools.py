#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Base

# Internal
from processing.objects.node import Node

# External
from OSMPythonTools.api import ApiResult


class NodeTools:
    @staticmethod
    def node_from_api(api_result: ApiResult) -> Node:
        node = Node(
            id=api_result.id(),
            lat=api_result.lat(),
            lon=api_result.lon(),
        )

        return node
