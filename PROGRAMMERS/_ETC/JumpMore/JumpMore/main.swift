//
//  main.swift
//  JumpMore
//
//  Created by In Taek Cho on 2020-10-19.
//

import Foundation

func solution(_ n:Int) -> Int64 {
    var arr: [Int64] = [1,2]
    var index = 0
    while arr.count < n {
        arr.append((arr[index] + arr[index + 1]) % 1234567)
        index += 1
    }

    return arr[n - 1]
}

//print(solution(2000))
