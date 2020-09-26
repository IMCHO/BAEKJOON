//
//  main.swift
//  Immigration
//
//  Created by In Taek Cho on 2020-09-25.
//

import Foundation

func solution(_ n:Int, _ times:[Int]) -> Int64 {
    var copiedTimes = times.map({ [Int64($0), Int64($0)] })
    var cnt = 0
    var minimum = [Int64]()
    
    while cnt != n {
        copiedTimes.sort(by: { $0[0] < $1[0] })
        minimum = copiedTimes.removeFirst()
        cnt += 1
        copiedTimes.insert([minimum[0] + minimum[1], minimum[1]], at: 0)
    }
    
    return minimum[0]
}

print(solution(6, [7,10]))

