import sys

if sys.version_info < (3, 10):
    from importlib_metadata import entry_points
else:
    from importlib.metadata import entry_points

print("hatch entry points:")

items = entry_points(group='hatch')
for item in items:
    print(item)
