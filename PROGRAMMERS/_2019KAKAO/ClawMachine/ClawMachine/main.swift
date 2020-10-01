//
//  main.swift
//  ClawMachine
//
//  Created by In Taek Cho on 2020-10-01.
//

import Foundation

func solution(_ board:[[Int]], _ moves:[Int]) -> Int {
    var result = [Int]()
    var stacks = [Int:[Int]]()
    var answer = 0
    
    for line in board {
        for (index, value) in line.enumerated() {
            if value == 0 { continue }
            if var list = stacks[index] {
                list.append(value)
                stacks[index] = list
            } else {
                stacks[index] = [value]
            }
        }
    }
    
    for move in moves {
        if var list = stacks[move - 1] {
            if list.count == 0 { continue }
            result.append(list.removeFirst())
            stacks[move - 1] = list
        }
        
        if result.count >= 2 {
            if result[result.count - 1] == result[result.count - 2] {
                result.removeLast()
                result.removeLast()
                answer += 2
            }
        }
    }
    
    return answer
}

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))
