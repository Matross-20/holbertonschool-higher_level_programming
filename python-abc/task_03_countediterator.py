class CountedIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0
    
    def __next__(self):
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration
    
    def get_count(self):
        return self.count
    
    def __iter__(self):
        return self

# Test script for CountedIterator

# Instantiate a CountedIterator object using a list
iterable = [1, 2, 3, 4, 5]
counted_iterator = CountedIterator(iterable)

# Iterate over items using a loop
for item in counted_iterator:
    print(item)  # Should print each item in the list

# Print the count of items iterated
print(f"Number of items iterated: {counted_iterator.get_count()}")
