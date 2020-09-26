//
//  main.swift
//  Immigration
//
//  Created by In Taek Cho on 2020-09-25.
//

import Foundation

func solution(_ n:Int, _ times:[Int]) -> Int64 {
    var minimum: Int64 = 1
    var worst: Int64 = times.map({Int64($0)}).sorted().last! * Int64(n)
    var result = [Int64]()
    
    while minimum <= worst {
        let mid = (worst + minimum) / 2
        let numberOfPerson = times.map({ mid / Int64($0) }).reduce(0, { $0 + $1 })
        if numberOfPerson >= n {
            worst = mid - 1
            result.append(mid)
        } else {
            minimum = mid + 1
        }
    }
    
    return result.sorted().first!
}

//print(solution(6, [7,10]))

