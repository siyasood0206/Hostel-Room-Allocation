
rooms = {
    101: {"capacity": 2, "students": []},
    102: {"capacity": 3, "students": []},
    103: {"capacity": 2, "students": []},
    104: {"capacity": 1, "students": []}
}
def check_vacancy():
    print("\n--- Available Rooms ---")

    for room, details in rooms.items():
        vacant = details["capacity"] - len(details["students"])

        if vacant > 0:
            print("Room", room, "Vacant Beds:", vacant)
def allocate_room(student_name, room_number):
    if not isinstance(student_name, str) or not student_name.strip():
        print("Invalid student name.")
        return
    if room_number not in rooms:
        print("Invalid room number.")
        return
    for details in rooms.values():
        if student_name in details["students"]:
            print("Student already allocated.")
            return
    room = rooms[room_number]
    if len(room["students"]) < room["capacity"]:
        room["students"].append(student_name)
        print(student_name, "allocated to room", room_number)
    else:
        print("Room is full!")
def occupancy_report():
    print("\n--- Hostel Occupancy Report ---")
    total_capacity = 0
    total_occupied = 0
    for room, details in rooms.items():
        capacity = details["capacity"]
        occupied = len(details["students"])
        vacant = capacity - occupied
        total_capacity += capacity
        total_occupied += occupied
        print("\nRoom:", room)
        print("Capacity:", capacity)
        print("Occupied:", occupied)
        print("Vacant:", vacant)
        print("Students:", details["students"])
    print("\nTotal Capacity:", total_capacity)
    print("Total Occupied:", total_occupied)
    print("Total Vacant:", total_capacity - total_occupied)
