# Your roommate tasks you with finding a new apartment on one condition: the view can't be blocked by another apartment.

# You're given a list of buildings, specifically apartment elevations. For some reason, the owners of each building have agreed to represent it as an array of integers denoting the height of each apartment (eg: [1, 2, 3, 4] or [19, 14, 21, 12, 5]).

# If one apartment height (eg: 1) is lesser than another apartment to its right (eg: 4), then the first apartment's view will be blocked.

# For example [1, 2, 3, 4] would only return [4]. In the case of [19, 14, 21, 12, 5], there would be multiple valid apartments ([21, 12, 5]).

def views(buildings):
  candidates = []
  for i, apt in enumerate(buildings):
    while candidates and buildings[i] > candidates[-1]:
      candidates.pop()
    candidates.append(apt)
  return candidates

print(views([1, 2, 3, 4])) # 4
print(views([19, 14, 21, 12, 5])) # [21, 12, 5]
