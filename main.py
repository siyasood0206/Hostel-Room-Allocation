
from hostel_pkg import (
    check_vacancy,
    allocate_room,
    occupancy_report
)
print("HOSTEL ROOM ALLOCATION SYSTEM")
check_vacancy()
allocate_room("Rahul", 101)
allocate_room("Priya", 101)
allocate_room("Aman", 102)
allocate_room("Sneha", 103)
allocate_room("Karan", 105)
allocate_room("Rahul", 102)
occupancy_report()
