//
//  main.swift
//  TriangleSnail
//
//  Created by In Taek Cho on 2020-10-30.
//

import Foundation

func solution(_ n:Int) -> [Int] {
    var result = [[Int]]()
    for i in 1...n {
        result.append(Array(repeating: 0, count: i))
    }
    
    var startPoint = 0
    var offset = 0
    var num = 1
    
    while true {
        for index in startPoint..<n - offset {
            if result[index][offset] == 0 {
                result[index][offset] = num
                num += 1
            }
        }
        
        for index in offset..<result[n - offset - 1].count - offset {
            if result[n - offset - 1][index] == 0 {
                result[n - offset - 1][index] = num
                num += 1
            }
        }
        
        for index in stride(from: n - offset - 2, through: offset + 1, by: -1) {
            if result[index][result[index].count - offset - 1] == 0 {
                result[index][result[index].count - offset - 1] = num
                num += 1
            }
        }
        
        startPoint += 2
        offset += 1
        
        if startPoint > n - offset {
            break
        }
    }
    
//    print(result)
    return result.reduce([], { $0 + $1})
}

//solution(1000)
