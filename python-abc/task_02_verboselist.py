#!/usr/bin/env python3
class VerboseList(list):
    
    def append(self, item):
        super().append(item)
        print(f"Added {item} to the list.")
    
    def extend(self, iterable):
        super().extend(iterable)
        print(f"Extended the list with {len(iterable)} items.")
    
    def remove(self, item):
        print(f"Removed {item} from the list.")
        super().remove(item)
    
    def pop(self, index=-1):
        item = super().pop(index)
        print(f"Popped {item} from the list.")
        return item

# Test script for VerboseList

# Instantiate a VerboseList object
vlist = VerboseList()

# Test the append method
vlist.append(10)  # Should print "Added 10 to the list."
vlist.append(20)  # Should print "Added 20 to the list."

# Test the extend method
vlist.extend([30, 40, 50])  # Should print "Extended the list with 3 items."

# Test the remove method
vlist.remove(20)  # Should print "Removed 20 from the list."

# Test the pop method
vlist.pop()  # Should print "Popped 50 from the list."
vlist.pop(0)  # Should print "Popped 10 from the list."

# The final state of the list should be [30, 40]
print(vlist)  # Should print [30, 40]
