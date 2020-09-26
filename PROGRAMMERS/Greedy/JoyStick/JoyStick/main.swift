//
//  main.swift
//  JoyStick
//
//  Created by In Taek Cho on 2020-09-26.
//

import Foundation

func solution(_ name:String) -> Int {
    var cnt = 0
    var posOfNotA = [Int]()
    
    for (index, value) in name.enumerated() {
        if value != "A" {
            posOfNotA.append(index)
        }
    }
    
    var now = 0
    var nearestPos = 0

    while posOfNotA.count != 0 {
        var temp = 26
        for pos in posOfNotA {
            let value = min(name.count - pos + now, pos - now)
            if temp > value {
                nearestPos = pos
                temp = value
            }
        }
        posOfNotA.remove(at: posOfNotA.firstIndex(of: nearestPos)!)
        cnt += min(name.count - nearestPos + now, nearestPos - now)
        now = nearestPos
        let destinationStr = String(name[name.index(name.startIndex, offsetBy: now)])
        cnt += Int(min(26 - (UnicodeScalar(destinationStr)!.value - 65), UnicodeScalar(destinationStr)!.value - 65))
    }
    
    return cnt
}

//print(solution("BAAAAAABB"))
//print(solution("BBAAAAA"))
//print(solution("BBAAAAAB"))

//print(solution("BBBBAAAABA")) // 12
//print(solution("BBBBAAAAAB")) // 10
print(solution("AABAAAAAAABBB")) // 12
//print(solution("AAB")) // 2
