#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Base
import numpy as np

# Internal
from processing.objects import Node, Way

# External
from OSMPythonTools.api import ApiResult


class MapTools:
    EARTH_RADIUS = 3958.75
    MILES_TO_KM = 1 / 0.62137119

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

    @staticmethod
    def distance_bulk(nodes1: list[list[Node]] | list[Node], nodes2: list[Node] | None = None,
                      units='km', r=EARTH_RADIUS) -> np.array:
        if nodes2 is None:
            nodes2 = [node[1] for node in nodes1]
            nodes1 = [node[0] for node in nodes1]

        assert len(nodes1) == len(nodes2), 'Length of nodes1 and nodes2 must be equal'
        assert units in ['km', 'ml'], 'Unit must be "km" or "ml"'

        pos1 = np.array([[node.lat, node.lon] for node in nodes1])
        pos2 = np.array([[node.lat, node.lon] for node in nodes2])

        pos1 = pos1 * np.pi / 180
        pos2 = pos2 * np.pi / 180

        cos_lat1 = np.cos(pos1[..., 0])
        cos_lat2 = np.cos(pos2[..., 0])
        cos_lat_d = np.cos(pos1[..., 0] - pos2[..., 0])
        cos_lon_d = np.cos(pos1[..., 1] - pos2[..., 1])

        result = r * np.arccos(cos_lat_d - cos_lat1 * cos_lat2 * (1 - cos_lon_d))

        return result if units == 'ml' else result * MapTools.MILES_TO_KM

    @staticmethod
    def distance(node1: Node, node2: Node, units='km', r=EARTH_RADIUS):
        return MapTools.distance_bulk([node1], [node2], units=units, r=r)[0]
