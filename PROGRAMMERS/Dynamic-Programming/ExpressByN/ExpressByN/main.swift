//
//  main.swift
//  ExpressByN
//
//  Created by In Taek Cho on 2020-09-18.
//

import Foundation

func solution(_ N:Int, _ number:Int) -> Int {
    var initial = [Int]()
    var BFS = [Array<Int>]()
    
    for cnt in 1...7 {
        let temp = Int(String(repeating: String(N), count: cnt))!
        initial.append(temp)
        BFS.append([temp, String(temp).count])
    }
    
    while BFS.count != 0 {
        let target = BFS.removeFirst()
        if target[1] > 8 {
             return -1
        }
        
        for offset in initial {
            let cnt = String(offset).count + target[1]
            let newValue1 = target[0] + offset
            let newValue2 = target[0] - offset
            let newValue3 = target[0] / offset
            let newValue4 = target[0] * offset
            
            if newValue1 == number || newValue2 == number || newValue3 == number || newValue4 == number {
                if cnt > 8 {
                    return -1
                } else {
                    return cnt
                }
            }
            
            if newValue1 != number {
                BFS.append([newValue1, cnt])
            }
            if newValue2 != number {
                BFS.append([newValue2, cnt])
            }
            if newValue3 != number {
                BFS.append([newValue3, cnt])
            }
            if newValue4 != number {
                BFS.append([newValue4, cnt])
            }
        }
        BFS.sort {
            $0[1] < $1[1]
        }
    }
    return -1
}

print(solution(5, 31168))
