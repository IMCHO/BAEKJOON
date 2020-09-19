//
//  main.swift
//  ExpressByN
//
//  Created by In Taek Cho on 2020-09-18.
//

import Foundation

func solution(_ N:Int, _ number:Int) -> Int {
    let cntOfNumber = String(number).count
    var initial = [Int]()
    var arr = [[Int]]()
    
    for i in 1...cntOfNumber {
        let temp = Int(String(repeating: String(N), count: i))!
        if temp == number {
            return String(temp).count
        }
        initial.append(temp)
        arr.append([temp, String(temp).count])
    }
    
    var startIndex = 0
    var endIndex = arr.count
    
    while true {
        var listForExtension = [[Int]]()
        for target in arr[startIndex..<endIndex] {
//            print(target)
            let num = target[0]
            let cnt = target[1]
            
            for offset in initial {
                if check(num + offset, with: number) {
                    if checkCount(cnt + String(offset).count) {
                        return cnt + String(offset).count
                    } else {
                        return -1
                    }
                }
                if check(num - offset, with: number) {
                    if checkCount(cnt + String(offset).count) {
                        return cnt + String(offset).count
                    } else {
                        return -1
                    }
                }
                if check(num / offset, with: number) {
                    if checkCount(cnt + String(offset).count) {
                        return cnt + String(offset).count
                    } else {
                        return -1
                    }
                }
                if check(num * offset, with: number) {
                    if checkCount(cnt + String(offset).count) {
                        return cnt + String(offset).count
                    } else {
                        return -1
                    }
                }
                    listForExtension.append([num + offset, cnt + String(offset).count])
                    listForExtension.append([num - offset, cnt + String(offset).count])
                    listForExtension.append([num * offset, cnt + String(offset).count])
                    listForExtension.append([num / offset, cnt + String(offset).count])
            }
        }
        startIndex = endIndex
        endIndex = endIndex + listForExtension.count
        arr += listForExtension
//        print(listForExtension)
    }
}

func check(_ value: Int, with answer: Int) -> Bool {
    if value == answer {
        return true
    } else {
        return false
    }
}

func checkCount(_ value: Int) -> Bool {
    if value <= 8 {
        return true
    } else {
        return false
    }
}


print(solution(5, 31168))
