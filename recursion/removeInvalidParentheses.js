function checkParens(array) {
  let count = 0;

  for (let i = 0; i < array.length; i++) {
    if (array[i] === '(') {
      count++;
    } else if (array[i] === ')') {
      count--;
      if (count < 0) return false;
    }
  }
  return count === 0;
}

function removeInvalid(str) {
  const array = str.split('');
  const resultSet = new Set();
  let removes = 0;
  let minRemoves = Number.MAX_VALUE;

  function helper(index) {
    if (index === array.length) {
      if (checkParens(array) && removes <= minRemoves) {
        resultSet.add(array.join(''));
        minRemoves = removes;
      }
      return;
    }
  
    // Try NOT removing this character first because we
    // want to find the minimum number of edits.
    helper(index + 1);

    const char = array[index];
    if (char === '(' || char === ')') {
      array[index] = null;
      removes++;
      helper(index + 1);
      removes--; // uncount
      array[index] = char;
    }
  }

  helper(0);

  return resultSet;
}
