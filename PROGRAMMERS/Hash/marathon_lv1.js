function solution(participant, completion) {
    var answer = '';

    for (let index = 0; index < participant.length; index++) {
        const element = participant[index];
        var numInP = participant.filter(name => name == element);
        var numInC = completion.filter(name => name == element);
        if (numInC.length == 0) {
            answer = element;
            return answer;
        }
        if (numInC.length != numInP.length) {
            answer = element;
            return answer;
        }
    }
}