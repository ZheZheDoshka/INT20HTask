#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Base
from unittest import TestCase

# Internal
from processing.objects import Node
from processing.tools.map_tools import MapTools

# External


class TstMapTools(TestCase):
    def test_distance(self):
        node1 = Node(0, 46.4384699, 30.7235512)
        node2 = Node(1, 47.4344699, 33.7335512)

        distance = MapTools.distance(node1, node2)
        self.assertEqual(distance, 253.9308995896021)

    def test_distance_bulk(self):
        node1 = Node(0, 46.4384699, 30.7235512)
        node2 = Node(1, 47.4344699, 33.7335512)
        node3 = Node(2, 48.4344699, 34.7335512)

        nodes1 = [node1, node2]
        nodes2 = [node2, node3]

        distances = MapTools.distance_bulk(nodes1, nodes2)
        self.assertEqual(distances[0], 253.9308995896021)
        self.assertEqual(distances[1], 133.84144107703224)

    def test_distance_bulk_one_list(self):
        node1 = Node(0, 46.4384699, 30.7235512)
        node2 = Node(1, 47.4344699, 33.7335512)
        node3 = Node(2, 48.4344699, 34.7335512)

        nodes1 = [[node1, node2], [node2, node3]]
        nodes2 = None

        distances = MapTools.distance_bulk(nodes1, nodes2)
        self.assertEqual(distances[0], 253.9308995896021)
        self.assertEqual(distances[1], 133.84144107703224)

    def test_distance_bulk_ml(self):
        node1 = Node(0, 46.4384699, 30.7235512)
        node2 = Node(1, 47.4344699, 33.7335512)
        node3 = Node(2, 48.4344699, 34.7335512)

        nodes1 = [node1, node2]
        nodes2 = [node2, node3]

        distances = MapTools.distance_bulk(nodes1, nodes2, 'ml')
        self.assertEqual(distances[0], 157.78534525576157)
        self.assertEqual(distances[1], 83.1652155133504)

    def test_distance_bulk_radius(self):
        node1 = Node(0, 46.4384699, 30.7235512)
        node2 = Node(1, 47.4344699, 33.7335512)
        node3 = Node(2, 48.4344699, 34.7335512)

        nodes1 = [node1, node2]
        nodes2 = [node2, node3]

        distances = MapTools.distance_bulk(nodes1, nodes2, r=1234)
        self.assertEqual(distances[0], 79.15395771230035)
        self.assertEqual(distances[1], 41.7203254282432)
