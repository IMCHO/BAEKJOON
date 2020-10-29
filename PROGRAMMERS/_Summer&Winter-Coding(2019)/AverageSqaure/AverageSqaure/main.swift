//
//  main.swift
//  AverageSqaure
//
//  Created by In Taek Cho on 2020-10-29.
//

import Foundation

func solution(_ w:Int, _ h:Int) -> Int64{
    let list: [Int64] = [w,h].map({Int64($0)}).sorted()
    var offset: Int64 = 0
    var num1: Int64 = 0
    var num2: Int64 = 0
    
    for i in stride(from: list[0], through: 1, by: -1) {
        if list[0] % i == 0 && list[1] % i == 0 {
            offset = i
            num1 = list[0] / i
            num2 = list[1] / i
            break
        }
    }
    return list[0] * list[1] - ((num1 + num2 - 1) * offset)
}
