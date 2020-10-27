'''
Booking Module
'''
from typing import Set, List
from datetime import date
import ipdb

from errors.errors import BookingRequirementNotMetException
from models.user import User
from models.hotel import Hotel
from models.booking import Booking
from models.room import RoomType, Room
from models.room_date import RoomDate
from db import room_dates, bookings
from utils.date_utils import getDatesInRange
from utils.logger import logger


class BookingRequirement:
    def __init__(self, hotel: Hotel, no_standard: int, no_deluxe: int,
                 no_luxury: int, from_date: date, to_date: date):
        self.hotel = hotel
        self.no_standard = no_standard
        self.no_deluxe = no_deluxe
        self.no_luxury = no_luxury
        self.from_date = from_date
        self.to_date = to_date


class BookingService:
    '''
    Represents a booking model in the system
    Will have a corresponding db
    '''
    @staticmethod
    def meets_requirements(br: BookingRequirement) -> bool:
        ipdb.set_trace()
        booking_dates = getDatesInRange(br.from_date, br.to_date)
        hotel = br.hotel

        # Checking current_capacity
        current_capacity = hotel.capacity
        for _date in booking_dates:
            _room_dates = [
                x for x in room_dates if x.date == _date and x.hotel == hotel
            ]
            # If there are no booked rooms in those dates, return True
            if len(_room_dates) == 0:
                return True
            # Check if the required room type is available
            for _room_date in _room_dates:
                _room = _room_date.room
                current_capacity[_room.room_type] -= 1

        # Checking if it meets requirement
        if br.no_standard > current_capacity[RoomType.STANDARD]:
            return False
        if br.no_luxury > current_capacity[RoomType.LUXURY]:
            return False
        if br.no_deluxe > current_capacity[RoomType.DELUXE]:
            return False
        if br.no_suite > current_capacity[RoomType.SUITE]:
            return False
        return True

    @staticmethod
    def getUnavailableRoomsInDateRange(hotel, from_date, to_date) -> Set[Room]:
        booking_dates = getDatesInRange(from_date, to_date)
        unavailable_rooms = set()
        for _date in booking_dates:
            _booked_rooms = {x.room for x in room_dates if x.date == _date}
            unavailable_rooms.union(_booked_rooms)
        return unavailable_rooms

    @staticmethod
    def getAvailableRoomsInDateRange(hotel, from_date, to_date) -> Set[Room]:
        unavailable_rooms = BookingService.getUnavailableRoomsInDateRange(
            hotel, from_date, to_date)
        return set(hotel.rooms).difference(unavailable_rooms)

    @staticmethod
    def pickNRoomOfType(available_rooms: Set[Room], room_type: RoomType,
                        number_required: int) -> Set[Room]:
        return set([x for x in available_rooms
                    if x.room_type == room_type][0:number_required])

    @staticmethod
    def book(user: User, hotel: Hotel, br: BookingRequirement) -> Booking:
        '''
        Books the set of rooms according to the BookingRequirement
        If the requirement is not met, raises
        '''
        ipdb.set_trace()
        logger.info('Finding available rooms')
        if not BookingService.meets_requirements(br):
            logger.error('Rooms not available matching the requirement')
            raise BookingRequirementNotMetException()

        logger.info('Finding available rooms...')
        available_rooms = BookingService.getAvailableRoomsInDateRange(
            hotel, br.from_date, br.to_date)
        logger.info('Found available rooms: ')
        logger.info(available_rooms)

        logger.info('Assigning rooms...')
        assigned_rooms = set()
        for room_type in [x.name for x in RoomType]:
            number = 0
            if room_type == RoomType.STANDARD:
                number = br.no_standard
            if room_type == RoomType.DELUXE:
                number = br.no_deluxe
            if room_type == RoomType.LUXURY:
                number = br.no_luxury
            if room_type == RoomType.SUITE:
                number = br.no_suite
            picked_rooms = BookingService.pickNRoomOfType(
                available_rooms, room_type, number)
            assigned_rooms.union(picked_rooms)

        logger.debug('Writing rooms to RoomDate')
        # Adding Room to RoomDate table
        for _assigned_room in assigned_rooms:
            for _date in getDatesInRange(br.from_date, br.to_date):
                room_date = RoomDate(_assigned_room, _date)
                room_dates.append(room_date)
        logger.debug('Finished writing rooms to RoomDate')

        booking = Booking(user, hotel, assigned_rooms, br.from_date,
                          br.to_date)
        bookings.append(booking)
        logger.info("Booking completed for user %s. Booking id: %s", user,
                    booking.booking_id)
        logger.info(booking)
        return booking

    def cancelBooking(self, user: User, booking_id: int):
        pass
