function atoi_iterative(str) {
  const map = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
    '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
  };
  let value = 0;
  const negative = str[0] === '-';
  let i = negative ? 1 : 0;

  for(; i < str.length; i++) {
    const digit = map[str[i]];
    value = value * 10 + digit;
  }

  return negative ? -value : value;
}

function atoi_recursive(str) {
  const map = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
    '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
  };

  function recursiveHelper(str, index, value = 0) {

    if (index === str.length) {
      return value;
    }

    const nextValue = value * 10 + map[str[index]];
    return recursiveHelper(str, index + 1, nextValue);
  }

  const negative = str[0] === '-';
  const start = negative ? 1 : 0;
  const value = recursiveHelper(str, start);

  return negative ? -value : value;
}
