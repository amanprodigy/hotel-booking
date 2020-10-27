from typing import Set
from datetime import date
from enum import Enum, unique
from uuid import uuid4, UUID


@unique
class RoomType(Enum):
    STANDARD = 'STANDARD'
    DELUXE = 'DELUXE'
    LUXURY = 'LUXURY'
    SUITE = 'SUITE'


class Room:
    '''
    Represents a Room in a system
    '''
    room_id: UUID
    size: int  # size of the room
    room_type: RoomType
    room_number: str
    booked_dates: Set[date]
    hotel_id: int

    def __init__(self, hotel_id: int, size: int, room_type: RoomType,
                 room_number: str):
        self.room_id = uuid4()
        self.hotel_id = hotel_id
        self.size = size
        self.room_type = room_type
        self.room_number = room_number

    def __str__(self):
        return f"Hotel: {self.hotel_id} Room number: {self.room_number}"

    def __repr__(self):
        return f"Hotel: {self.hotel_id} Room number: {self.room_number}"
