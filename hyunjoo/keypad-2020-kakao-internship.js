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
// https://programmers.co.kr/learn/courses/30/lessons/67256/solution_groups?language=javascript
// The key idea is that the x-axis distance is ZERO when it's the middle of column-2,5,8, and
// same distance which is ONE in both side columns.

function solution(numbers, hand) {
  hand = hand[0] === "r" ? "R" : "L";
  const ROW = [1, 4, 4, 4, 3, 3, 3, 2, 2, 2]; // row number of 0 - 9 (y axis)
  const COLUMN = {
    CENTER: 0,
    SIDE: 1,
  };
  let h = { L: { x: COLUMN.SIDE, y: 1 }, R: { x: COLUMN.SIDE, y: 1 } };

  return numbers
    .map((num) => {
      if (/[147]/.test(num)) {
        // Left numbers
        h.L.x = COLUMN.SIDE;
        h.L.y = ROW[num];
        return "L";
      } else if (/[369]/.test(num)) {
        // Right numbers
        h.R.x = COLUMN.SIDE;
        h.R.y = ROW[num];
        return "R";
      } else {
        // Middle numbers
        const distL = Math.abs(ROW[num] - h.L.y) + h.L.x;
        const distR = Math.abs(ROW[num] - h.R.y) + h.R.x;
        if (distL === distR) {
          h[hand].x = COLUMN.SIDE;
          h[hand].y = ROW[num];
          return hand;
        } else if (distL < distR) {
          h.L.x = COLUMN.CENTER;
          h.L.y = ROW[num];
          return "L";
        } else {
          h.R.x = COLUMN.CENTER;
          h.R.y = ROW[num];
          return "R";
        }
      }
    })
    .join("");
}
