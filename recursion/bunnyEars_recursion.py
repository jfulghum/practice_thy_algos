def bunnyEars(bunnies: int) -> int:
  if bunnies == 0:
    return 0

  return 2 + bunnyEars(bunnies - 1)


print(bunnyEars(8))
