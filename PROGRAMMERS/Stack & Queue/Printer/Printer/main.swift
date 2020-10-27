//
//  main.swift
//  Printer
//
//  Created by In Taek Cho on 2020-10-27.
//

import Foundation

func solution(_ priorities:[Int], _ location:Int) -> Int {
    var prioritiesWithIndex = priorities.enumerated().map({[$0.0, $0.1]})
    var result = [[Int]]()
    var answer = 0
    
    while prioritiesWithIndex.count != 0 {
        let value = prioritiesWithIndex.removeFirst()
        var isHigher = true
        
        for target in prioritiesWithIndex {
            if value[1] < target[1] {
                prioritiesWithIndex.append(value)
                isHigher = false
                break
            }
        }
        
        if isHigher {
            result.append(value)
        } else {
            continue
        }
    }
    
    for (index, r) in result.enumerated() {
        if r[0] == location {
            answer = index + 1
        }
    }
    return answer
}
