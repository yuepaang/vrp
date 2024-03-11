# -*- coding: utf-8 -*-
""".



__author__ = Yue Peng
__copyright__ = Copyright 2024
__version__ = 0.0.1
__maintainer__ = Yue Peng
__email__ = yuepaang@gmail.com
__status__ = Dev
__filename__ = env.py
__uuid__ = c0fd3eee-cb2b-4635-beee-dc7dfaef1947
__date__ = 2024-03-11 15:19:00
__modified__ =
"""


from typing import List


class Vehicle(object):
    def __init__(self, id: int, capacity: float, speed: float) -> None:
        self.id = id
        self.capacity = capacity
        self.speed = speed


class Node(object):
    def __init__(
        self,
        location: int,
        service_time: float,
        start_time: float,
        end_time: float,
    ) -> None:
        self.location = location
        self.service_time = service_time
        self.start_time = start_time
        self.end_time = end_time


class VehicleNode(object):
    def __init__(self, vehicle: Vehicle, node: Node) -> None:
        self.vehicle = vehicle
        self.node = node


class Customer(object):
    def __init__(
        self, id: int, demand: float, customer_type: int, brother_id: int
    ) -> None:
        self.id = id
        self.demand = demand
        self.customer_type = customer_type
        self.brother_id = brother_id


class CustomerNode(object):
    def __init__(self, customer: Customer, node: Node) -> None:
        self.customer = customer
        self.node = node


class Depot(object):
    def __init__(self, location: int, vehicles: List[VehicleNode]) -> None:
        self.location = location
        self.vehicles = vehicles


class Env(object):
    def __init__(
        self,
        depots: List[Depot],
        customers: List[CustomerNode],
        dist: List[List[float]],
    ) -> None:
        self.depots = depots
        self.customers = customers
        self.dist = dist
