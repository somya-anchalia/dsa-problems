def mostBookedRoom(rooms):
    booking_count = {}
    
    for entry in rooms:
        action = entry[0]
        room = entry[1:]
        
        if action == '+':
            if room in booking_count:
                booking_count[room] += 1
            else:
                booking_count[room] = 1
    
    max_booked_room = None
    max_bookings = 0
    
    for room, count in booking_count.items():
        if count > max_bookings or (count == max_bookings and room < max_booked_room):
            max_booked_room = room
            max_bookings = count
    
    return max_booked_room

# Example usage
rooms = ["+1A", "+3E", "-1A", "-3E", "+1A", "+3E", "+4F", "-3E", "+3E"]
print(mostBookedRoom(rooms))  # Output: "1A"
