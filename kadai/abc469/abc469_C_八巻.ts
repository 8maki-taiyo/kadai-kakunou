import { readFileSync } from "node:fs";

function main(N: number, S: string): void {
    // 考え方:
    // o 袋を 1 個捨てると、次の袋を 1 個受け取れる。
    // 次の袋が o なら、捨てた分の o 袋を取り戻せる。
    // 次の袋が x なら、o 袋を取り戻せず、手持ちの o 袋が 1 個減る。
    //
    // つまり、x を 1 個受け取るたびに、追加で袋を取れる回数が 1 回減る。
    // k 個目の x を受け取ったところで袋を取れなくなるため、
    // k の答えは「k 個目の x の位置」である。

    // 1. x がある位置を、左から順に記録する
    const xPositions: number[] = [];
    for (let i = 0; i < N; i++) {
        if (S[i] === "x") {
            xPositions.push(i + 1);
        }
    }

    // 2. k 個目の x の位置を答えとして出力する
    let result: number = 0;
    for (let k = 1; k <= N; k++) {
        // 3. k 個目の x があれば、その位置で o 袋を使い切る
        // k 個目の x がなければ、最後まで袋を受け取れるので答えは N
        result = xPositions[k - 1] ?? N;

        console.log(result);
    }
}

const input = readFileSync(0, "utf8").trim().split(/\s+/);
const N = Number(input[0]);
const S = input[1];

main(N, S);
