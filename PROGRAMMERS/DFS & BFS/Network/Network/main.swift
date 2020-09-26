//
//  main.swift
//  Network
//
//  Created by In Taek Cho on 2020-09-26.
//

import Foundation

func solution(_ n:Int, _ computers:[[Int]]) -> Int {
    var infos = [Int:[Int]]()
    for index in 0..<n {
        infos[index] = []
    }
    
    for x in 0..<n {
        for y in 0..<n {
            if x == y {
                continue
            }
            
            if computers[x][y] == 0 { continue }
            if var list = infos[x] {
                list.append(y)
                infos[x] = list
            } else {
                infos[x] = [y]
            }
        }
    }
    
    var stack = [0]
    var cntOfNetwork = 0
    var visited = Array(repeating: false, count: n)
    
    while stack.count != 0 {
        let topValue = stack.last!
        if !visited[topValue] {
            visited[topValue] = true
        }
        
        if infos[topValue]?.count != 0 {
            if var list = infos[topValue] {
                let value = list.removeFirst()
                infos[topValue] = list
                if !visited[value] {
                    stack.append(value)
                }
            }
        } else {
            stack.removeLast()
        }
        
        if stack.count == 0 {
            cntOfNetwork += 1
            if let value = infos.filter({ !visited[$0.key] }).keys.first {
                stack.append(value)
            }
        }
    }
    return cntOfNetwork
}

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
