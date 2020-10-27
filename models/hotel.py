'''
Hotel class
'''

from uuid import uuid4, UUID
from typing import List
from enum import Enum, unique

from models.room import RoomType, Room


class RoomInput:
    size: int
    room_type: RoomType
    room_number: str


class CapacityInput:
    standard: int
    deluxe: int
    luxury: int
    suite: int


@unique
class Stars(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5


class Hotel:
    '''
    Describes the hotel entity
    '''
    hotel_id: UUID
    name: str
    stars: Stars
    rooms: List[Room]
    capacity: dict

    def __init__(self, name: str, stars: Stars):
        self.hotel_id = uuid4()
        self.name = name
        self.stars = stars
        self.capacity = {
            RoomType.STANDARD: 0,
            RoomType.DELUXE: 0,
            RoomType.LUXURY: 0,
            RoomType.SUITE: 0,
        }
        self.rooms = []

    def get_name(self) -> str:
        return self.name

    def get_capacity_of_room_type(self, room_type: RoomType):
        return self.capacity[room_type]

    def add_rooms(self, room_inputs: List[RoomInput]):
        for room_input in room_inputs:
            room = Room(self.hotel_id, room_input[0], room_input[1],
                        room_input[2])
            self.rooms.append(room)
            # update capacity while adding rooms
            self.capacity[room_input[1]] += 1

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
