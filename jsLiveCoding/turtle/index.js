function turtle(hill, move, rollDown) {
  let target = 0;
  let days = 0;
  while (target < hill) {
    target += move;
    target -= rollDown;
    days++;
  }
  return days;
}
// turtle(100,50,30) -> 5
