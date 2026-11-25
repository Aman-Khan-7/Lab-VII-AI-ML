log1_list = ["A101", "B202", "C303", "A101", "D404"]
log1_events = set(log1_list)
log2_events = {"C303", "E505", "F606", "B202"}

common_events = log1_events.intersection(log2_events)
all_events = log1_events.union(log2_events)

print("Unique log1 events:", log1_events)
print("Common events (Intersection):", common_events)
print("All unique events (Union):", all_events)
