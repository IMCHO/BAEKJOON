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
    var minimun = 9
    while BFS.count != 0 {
        let target = BFS.removeFirst()
        
        for offset in initial {
            let cnt = String(offset).count + target[1]
            let newValue1 = target[0] + offset
            let newValue2 = target[0] - offset
            let newValue22 = offset - target[0]
            let newValue3 = target[0] / offset
            var newValue33: Int?
            if target[0] != 0 {
                newValue33 = offset / target[0]
            }
            let newValue4 = target[0] * offset
            
            if cnt > 8 {
                continue
            }

            if newValue1 == number || newValue2 == number || newValue22 == number || newValue3 == number || newValue4 == number {
                minimun = min(minimun, cnt)
            }
            
            if let value = newValue33 {
                if value == number {
                    minimun = min(minimun, cnt)
                } else {
                    BFS.append([value, cnt])
                }
            }
            
            if newValue1 != number {
                BFS.append([newValue1, cnt])
            }
            if newValue2 != number {
                BFS.append([newValue2, cnt])
            }
//            if newValue22 != number {
//                BFS.append([newValue22, cnt])
//            }
            if newValue3 != number {
                BFS.append([newValue3, cnt])
            }
            if newValue4 != number {
                BFS.append([newValue4, cnt])
            }
        }
    }
    return minimun >= 9 ? -1 : minimun
}

print(solution(5, 12))
