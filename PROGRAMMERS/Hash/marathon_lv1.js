function solution(participant, completion) {
    var answer = '';

    var people = {};
    participant.forEach(element => {
        if (!people[element]) {
            people[element] = 1;
        } else {
            people[element] += 1;
        }
    });

    completion.forEach(element => {
        people[element] -= 1;
    });

    for (let index = 0; index < participant.length; index++) {
        const element = people[participant[index]];
        if (element != 0) {
            answer = participant[index];
            return answer;
        }
    }
}