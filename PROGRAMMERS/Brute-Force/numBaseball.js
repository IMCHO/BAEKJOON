function solution(baseball) {
    var answer = [];
    let sortedBaseball = baseball.sort((b1, b2) => {
        if (b1[1] + b1[2] == b2[1] + b2[2]) {
            return b2[1] - b1[1];
        }
        return (b2[1] + b2[2]) - (b1[1] + b1[2]);
    });

    let num = 111;
    while (num != 1000) {
        for (const key in sortedBaseball) {
            if (sortedBaseball.hasOwnProperty(key)) {
                let element = sortedBaseball[key];
                let expectedAns = num + '';
                let hint = element[0] + '';
                let strike = 0;
                let ball = 0;

                if (expectedAns[0] === expectedAns[1] || expectedAns[1] === expectedAns[2] || expectedAns[0] === expectedAns[2] || expectedAns.indexOf('0') > 0) break;

                for (let index = 0; index < expectedAns.length; index++) {
                    if (expectedAns[index] === hint[index]) strike++;
                    else {
                        if (expectedAns.indexOf(hint[index]) != -1) ball++;
                    }
                }

                if (strike !== element[1] || ball !== element[2]) break;

                if (key == sortedBaseball.length - 1) {
                    answer.push(num);
                }
            }
        }
        num++;
    }

    return answer.length;
}