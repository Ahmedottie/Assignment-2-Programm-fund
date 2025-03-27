
#hotel.py
class Hotel:
    def __init__(self, name, address):
        self.__name = name
        self.__address = address
        self.__rooms = []

    def add_room(self, room):
        self.__rooms.append(room)

    def get_available_rooms(self):
        return [room for room in self.__rooms if room.is_available()]

    def __str__(self):
        return f"Hotel: {self.__name}, Address: {self.__address}"

#room.py
class Room:
    def __init__(self, room_number, room_type, amenities, price):
        self.__room_number = room_number
        self.__room_type = room_type
        self.__amenities = amenities
        self.__price = price
        self.__available = True

    def book(self):
        self.__available = False

    def free(self):
        self.__available = True

    def is_available(self):
        return self.__available

    def __str__(self):
        return f"Room {self.__room_number} ({self.__room_type}) - ${self.__price}/night"

#guest.py
class Guest:
    def __init__(self, name, email, contact, loyalty_status='None'):
        self.__name = name
        self.__email = email
        self.__contact = contact
        self.__loyalty_status = loyalty_status
        self.__bookings = []

    def add_booking(self, booking):
        self.__bookings.append(booking)

    def view_bookings(self):
        return self.__bookings

    def __str__(self):
        return f"Guest: {self.__name}, Email: {self.__email}"

#booking.py
class Booking:
    def __init__(self, booking_id, guest, room, check_in, check_out):
        self.__booking_id = booking_id
        self.__guest = guest
        self.__room = room
        self.__check_in = check_in
        self.__check_out = check_out
        self.__payment = None
        self.__invoice = None
        room.book()

    def assign_payment(self, payment):
        self.__payment = payment

    def assign_invoice(self, invoice):
        self.__invoice = invoice

    def cancel(self):
        self.__room.free()

    def __str__(self):
        return f"Booking #{self.__booking_id} for {self.__guest}"

#payment.py
class Payment:
    def __init__(self, amount, method):
        self.__amount = amount
        self.__method = method
        self.__status = 'Pending'

    def process(self):
        self.__status = 'Completed'

    def __str__(self):
        return f"Payment: {self.__amount} via {self.__method} [{self.__status}]"

#invoice.py
class Invoice:
    def __init__(self, invoice_id, details, total):
        self.__invoice_id = invoice_id
        self.__details = details
        self.__total = total

    def __str__(self):
        return f"Invoice #{self.__invoice_id}: {self.__details} - Total: ${self.__total}"

#feedback.py
class Feedback:
    def __init__(self, guest, rating, comment):
        self.__guest = guest
        self.__rating = rating
        self.__comment = comment

    def __str__(self):
        return f"Feedback from {self.__guest}: {self.__rating}/5 - {self.__comment}"

# service_request.py
class ServiceRequest:
    def __init__(self, guest, req_type):
        self.__guest = guest
        self.__req_type = req_type
        self.__status = 'Pending'

    def mark_done(self):
        self.__status = 'Done'

    def __str__(self):
        return f"Request: {self.__req_type} by {self.__guest} [{self.__status}]"

#main.py
def run():
    from datetime import date
    hotel = Hotel("Royal Stay", "123 Palm Ave")
    room1 = Room(101, "Single", ["Wi-Fi", "TV"], 150)
    room2 = Room(102, "Double", ["Wi-Fi", "TV", "Mini-bar"], 200)
    hotel.add_room(room1)
    hotel.add_room(room2)

    print("Available Rooms:")
    for r in hotel.get_available_rooms():
        print(r)

    guest = Guest("Ahmed", "ahmed@example.com", "0501234567", "Gold")
    booking = Booking(1, guest, room1, date(2025, 3, 28), date(2025, 3, 30))
    guest.add_booking(booking)

    payment = Payment(300, "Credit Card")
    payment.process()
    booking.assign_payment(payment)

    invoice = Invoice(1, "2 nights in Room 101", 300)
    booking.assign_invoice(invoice)

    feedback = Feedback(guest, 5, "Fire stay, would book again 🔥")
    print(feedback)

    req = ServiceRequest(guest, "Room Cleaning")
    req.mark_done()
    print(req)

    print(booking)
    print(invoice)
    print(payment)

    print("Available Rooms After Booking:")
    for r in hotel.get_available_rooms():
        print(r)

if __name__ == "__main__":
    run()

#Part C - Test cases
from datetime import date

#guest account creation test
guest1 = Guest("Ahmed", "ahmed@example.com", "0501111111", "Gold")
guest2 = Guest("Ali", "ali@example.com", "0502222222", "Silver")
print(guest1)
print(guest2)

#add some rooms to search from
room1 = Room(201, "Single", ["Wi-Fi"], 100)
room2 = Room(202, "Double", ["Wi-Fi", "TV"], 150)
room3 = Room(203, "Suite", ["Wi-Fi", "TV", "Mini-bar"], 300)
hotel = Hotel("Royal Stay", "Somewhere")
hotel.add_room(room1)
hotel.add_room(room2)
hotel.add_room(room3)

#search available rooms test
print("Available rooms:")
for room in hotel.get_available_rooms():
    print(room)

#book two rooms
booking1 = Booking(101, guest1, room1, date(2025, 4, 1), date(2025, 4, 3))
guest1.add_booking(booking1)
booking2 = Booking(102, guest2, room2, date(2025, 4, 5), date(2025, 4, 7))
guest2.add_booking(booking2)

#simulate booking confirmation
print(f"Booking confirmed for {guest1}")
print(f"Booking confirmed for {guest2}")

#generate invoices
invoice1 = Invoice(201, "2 nights in Room 201", 200)
invoice2 = Invoice(202, "2 nights in Room 202", 300)
booking1.assign_invoice(invoice1)
booking2.assign_invoice(invoice2)
print(invoice1)
print(invoice2)

#different payment methods test
payment1 = Payment(200, "Credit Card")
payment1.process()
booking1.assign_payment(payment1)

payment2 = Payment(300, "Mobile Wallet")
payment2.process()
booking2.assign_payment(payment2)

print(payment1)
print(payment2)

#reservation history test
print("Ahmed's bookings:")
for b in guest1.view_bookings():
    print(b)

print("Ali's bookings:")
for b in guest2.view_bookings():
    print(b)

#cancel one booking
booking2.cancel()
print(f"Room {room2} cancelled and now available: {room2.is_available()}")

#extra test for room availability after cancel
print("Available rooms after cancellation:")
for room in hotel.get_available_rooms():
    print(room)
