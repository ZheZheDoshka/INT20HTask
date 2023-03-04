#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Base
from datetime import datetime

# Internal
from processing.objects import Node

# External
import pandas as pd
from meteostat import Point, Hourly


class WeatherTools:
    @staticmethod
    def weather_bulk(start_date: datetime, end_date: datetime, node: Node | Point | int) -> pd.DataFrame:
        if isinstance(node, Node):
            point = Point(node.lat, node.lon)
            point.get_stations(start=start_date, end=end_date)
            station_id = point.stations.item()

        elif isinstance(node, Point):
            node.get_stations(start=start_date, end=end_date)
            station_id = node.stations.item()

        elif isinstance(node, int):
            station_id = node

        else:
            raise TypeError('node must be Node, Point, or int')

        data = Hourly(station_id, start_date, end_date)
        return data.fetch()

    @staticmethod
    def weather(date: datetime, node: Node | Point | int) -> pd.Index:
        start_date = date.replace(minute=0, second=0, microsecond=0)
        end_date = date.replace(minute=59, second=59, microsecond=999999)

        data = WeatherTools.weather_bulk(start_date, end_date, node)

        return data.iloc[0]
