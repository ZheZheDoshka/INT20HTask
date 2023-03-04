#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Base

# Internal
from processing.objects import Node, Way

# External
from OSMPythonTools.api import ApiResult


class MapTools:
    @staticmethod
    def node_from_api(api_result: ApiResult) -> Node:
        node = Node(
            id=api_result.id(),
            lat=api_result.lat(),
            lon=api_result.lon(),
        )

        return node

    @staticmethod
    def way_from_api(api_result: ApiResult) -> Way:
        nodes = [MapTools.node_from_api(node) for node in api_result.nodes()]

        way = Way(
            id=api_result.id(),
            nodes=nodes,
        )

        return way
