// Delivery Active Time

// You are given a series of inputs representing delivery events. Each event is represented by an array of length 3:

// [1, 1591846068, 0]

// The first element is an order number

// The second is the timestamp

// The third is either 0 (representing a pickup) or 1 (representing a dropoff)

// Given a series of events, return the total active time, calculated by the period of time where they have an active delivery (if they've dropped everything off, they are not considered active until they pick something up again).

// Examples

// Input:
// [1, 1591846068, 0]
// [2, 1591846070, 0]
// [1, 1591846071, 1]
// [2, 1591846080, 1]
// [3, 1591846090, 0]
// [3, 1591846102, 1]

// Output: 24

// Function Signature

// func activeDeliveryTime(events: [[Int]]) -> Int

// Approach

// 1. Keep a counter, and an active time start timestamp
// 2. If counter is 0 when picking up an order, save timestamp
// 3. Increemnt when getting new order, decrement when dropping off order
// 4. When counter reaches 0, take difference of last dropped off delivery timestamp and active start time timestamp
// 5. Repeat until all orders are "processed"

// Followup:

// Only ask this as a followup if the interviewee(s) have fully solved the main prompt.

// Now, let's say the input is not guaranteed to be valid. What are some ways that the input could be invalid?

// - A single delivery has multiple pick ups or drop offs
// - Only one of pick up or drop off event for a delivery
// - Events can be out of order
//   - Sort orders by timestamp

const findActiveDeliveryTime = (arrOfEvents) => {
  let numOfActiveDeliveries = 0; 
  let startActiveTime = 0;
  let totalActiveTime = 0;  

  for(let i = 0; i < arrOfEvents.length; i++) {
    // Pick up delivery
    if (arrOfEvents[i][2] == 0) {
      if (numOfActiveDeliveries == 0) {
        startActiveTime = arrOfEvents[i][1]
      } 
      
      numOfActiveDeliveries++
    } else {
      // Drop off delivery
      if (numOfActiveDeliveries == 1) {
        totalActiveTime += arrOfEvents[i][1] - startActiveTime 
      }

      numOfActiveDeliveries--
    }
  }
  return totalActiveTime
}

console.log(findActiveDeliveryTime([]), ' == 0') // 0
let array = [[1, 1591846068, 0],
[2, 1591846070, 0],
[1, 1591846071, 1],
[2, 1591846080, 1],
[3, 1591846090, 0],
[3, 1591846102, 1]]

console.log(findActiveDeliveryTime(array), ' == 24')// 24


