# -*- coding: utf-8 -*-
"""VRP solver.

https://www.sintef.no/projectweb/top/pdptw/documentation/

__author__ = Yue Peng
__copyright__ = Copyright 2024
__version__ = 0.0.1
__maintainer__ = Yue Peng
__email__ = yuepaang@gmail.com
__status__ = Dev
__filename__ = main.py
__uuid__ = a10f6cee-7dc7-4f09-a28c-1ddcddb173e0
__date__ = 2024-03-11 15:10:08
__modified__ =
"""
import math
from typing import Tuple
from env import Customer, CustomerNode, Depot, Env, Vehicle, VehicleNode, Node


field_to_idx = {
    0: "task_no",
    1: "x",
    2: "y",
    3: "demand",
    4: "start_time",
    5: "end_time",
    6: "service_time",
    7: "pickup_id",
    8: "delivery_id",
}


def get_env_from_file(path: str) -> Tuple[Env, float]:
    customers = []
    positions = []
    wide = 0
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        header_info = lines[0].split("\t")
        capacity = float(header_info[1])
        for line in lines[1:]:
            fields = line.split("\t")
            index = int(fields[0])
            x = int(fields[1])
            y = int(fields[2])
            demand = float(fields[3])
            start_time = float(fields[4])
            end_time = float(fields[5])
            service_time = float(fields[6])
            pickup_id = int(fields[7])
            delivery_id = int(fields[8])
            if index == 0:
                depots = [
                    Depot(
                        0,
                        [
                            VehicleNode(
                                Vehicle(
                                    0,
                                    capacity,
                                    1,
                                ),
                                Node(0, service_time, start_time, end_time),
                            )
                        ],
                    )
                ]
            else:
                if pickup_id == 0:
                    customer_type = 1
                    brother_id = delivery_id - 1
                else:
                    customer_type = 2
                    brother_id = pickup_id - 1
                customers.append(
                    CustomerNode(
                        Customer(
                            index - 1,
                            demand,
                            customer_type,
                            brother_id,
                        ),
                        Node(index, service_time, start_time, end_time),
                    )
                )
            positions.append((x, y))
            if x > wide:
                wide = x
            if y > wide:
                wide = y
        dist = [
            [0 for _ in range(len(customers) + 1)] for _ in range(len(customers) + 1)
        ]
        for i in range(len(dist)):
            for j in range(len(dist)):
                x = abs(positions[i][0] - positions[j][0])
                y = abs(positions[i][1] - positions[j][1])
                dist[i][j] = math.sqrt(x * x + y * y)
        return Env(depots, customers, dist), wide


if __name__ == "__main__":
    env, t0 = get_env_from_file("./LC1_2_2.txt")
    print(env.dist[0][11], env.dist[27][13])
    print(env.customers[11].customer.customer_type)
    print(env.customers[11].customer.brother_id)
    print(t0)
