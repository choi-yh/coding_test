/*
 * https://programmers.co.kr/learn/courses/30/lessons/67256
 * Input/Output examples
 * numbers	                          hand	  result
 * [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	"right"	"LRLLLRLLRRL"
 * [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]	"left"	"LRLLRRLLLRR"
 * [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]	    "right"	"LLRLLRLLRL"
 */
// 1. First code
function solution(numbers, hand) {
  var answer = "";
  let lFingerPos = { x: 0, y: 3 };
  let rFingerPos = { x: 2, y: 3 };
  const POSDEF = {
    1: { x: 0, y: 0 },
    2: { x: 1, y: 0 },
    3: { x: 2, y: 0 },
    4: { x: 0, y: 1 },
    5: { x: 1, y: 1 },
    6: { x: 2, y: 1 },
    7: { x: 0, y: 2 },
    8: { x: 1, y: 2 },
    9: { x: 2, y: 2 },
    0: { x: 1, y: 3 },
  };

  function moveLeftHand(pos) {
    answer += "L";
    lFingerPos = pos;
  }

  function moveRightHand(pos) {
    answer += "R";
    rFingerPos = pos;
  }

  for (let n of numbers) {
    let pos = POSDEF[n];
    if (pos.x === 0) {
      moveLeftHand(pos);
    } else if (pos.x === 2) {
      moveRightHand(pos);
    } else {
      let lDiff =
        Math.abs(pos.x - lFingerPos.x) + Math.abs(pos.y - lFingerPos.y);
      let rDiff =
        Math.abs(pos.x - rFingerPos.x) + Math.abs(pos.y - rFingerPos.y);
      if (lDiff > rDiff) {
        moveRightHand(pos);
      } else if (lDiff < rDiff) {
        moveLeftHand(pos);
      } else {
        if (hand === "left") {
          moveLeftHand(pos);
        } else {
          moveRightHand(pos);
        }
      }
    }
  }
  return answer;
}

// 2. After refering
// TODO
