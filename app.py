from datetime import date

from models.hotel import Hotel, Stars
from models.room import RoomType
from models.user import User
from models.booking import Booking
from services.user_service import register_user
from services.booking_service import BookingService, BookingRequirement
from db import hotels, bookings


class App:
    '''
    Application class
    '''
    @staticmethod
    def init_app():
        print('Starting the hotel booking app...')
        taj = Hotel('Taj', Stars.FIVE)
        taj.add_rooms([
            (2, RoomType.STANDARD, '101'),
            (3, RoomType.DELUXE, '102'),
            (3, RoomType.LUXURY, '103'),
            (2, RoomType.STANDARD, '201'),
            (5, RoomType.LUXURY, '301'),
            (5, RoomType.LUXURY, '302'),
            (5, RoomType.LUXURY, '303'),
        ])

        radisson = Hotel('Radisson', Stars.FOUR)
        radisson.add_rooms([
            (2, RoomType.STANDARD, '101'),
            (2, RoomType.STANDARD, '102'),
            (3, RoomType.DELUXE, '103'),
            (2, RoomType.STANDARD, '201'),
            (2, RoomType.STANDARD, '202'),
            (6, RoomType.LUXURY, '301'),
            (6, RoomType.LUXURY, '302'),
            (3, RoomType.DELUXE, '401'),
            (4, RoomType.LUXURY, '402'),
            (5, RoomType.SUITE, '501'),
        ])
        print(taj)
        print(radisson)
        hotels.append(taj)
        hotels.append(radisson)

    @staticmethod
    def showBookings() -> None:
        print(bookings)

    @staticmethod
    def bookRequirement(user: User, hotel: Hotel,
                        br: BookingRequirement) -> Booking:
        return BookingService.book(user, hotel, br)


if __name__ == '__main__':
    App.init_app()
    App.showBookings()
    aman = register_user('Aman', 30, 'amanprodigy@gmail.com')
    print(aman)
    taj = hotels[0]
    sep1 = date(2020, 9, 1)
    sep3 = date(2020, 9, 3)
    br = BookingRequirement(taj, 2, 1, 1, sep1, sep3)
    booking = App.bookRequirement(aman, taj, br)
    print(booking)
