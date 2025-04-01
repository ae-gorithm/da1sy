function solution(input) {
  const [N, L] = input[0].split(" ").map(Number); // N: 물이 새는 곳의 개수, L: 테이프의 길이
  const positions = input[1].split(" ").map(Number); // 물이 새는 곳의 위치

  positions.sort((a, b) => a - b); // 오름차순 정렬

  let tapeCount = 0; // 필요한 테이프 개수
  let tapeCoverEnd = 0; // 현재 붙인 테이프가 막을 수 있는 마지막 위치

  for (let i = 0; i < N; i++) {
    const leak = positions[i];

    if (leak <= tapeCoverEnd) continue;

    tapeCount++;
    tapeCoverEnd = leak - 0.5 + L;
  }

  console.log(tapeCount);
}

// 백준 제출
// const input = require("fs")
//   .readFileSync("/dev/stdin")
//   .toString()
//   .trim()
//   .split("\n");

// solution(input);

// 로컬 테스트
const input = ["4 2", "1 2 100 101"];
solution(input);
