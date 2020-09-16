//
//  main.swift
//  FindPrime
//
//  Created by In Taek Cho on 2020-09-16.
//  Copyright © 2020 dlsxor21c. All rights reserved.
//

import Foundation

func solution(_ numbers:String) -> Int {
    var info: [Int:Array<Int>] = [:]
    
    for cnt in 1...numbers.count {
        info[cnt] = []
    }
    
    for cnt in 1...numbers.count {
        var copiedCnt = cnt
        while info[copiedCnt]?.count != numbers.count.makeCombination(with: copiedCnt) {
            var index: [Int] = []
            while index.count != copiedCnt {
                let randomIndex = Int.random(in: 0..<numbers.count)
                if !index.contains(randomIndex) {
                    index.append(randomIndex)
                }
            }
            var number: String = index.map({String(numbers[numbers.index(numbers.startIndex, offsetBy: $0)])}).reduce("", {$0 + $1})
            while true {
                if number[number.startIndex] == "0" {
                    number.removeFirst()
                    copiedCnt -= 1
                } else {
                    break
                }
            }
            if number == "" {
                continue
            }
            if !(info[copiedCnt]?.contains(Int(number)!))! {
                info[copiedCnt]?.append(Int(number)!)
            }
        }
    }
    
    print(info[1])
    
    var result = 0
    
    for (_, value) in info {
        for num in value {
            if num.checkPrime() {
                result += 1
            }
        }
    }
    
    return result
}

extension Int {
    func checkPrime() -> Bool {
        if self == 0 || self == 1 {
            return false
        }
        
        if self == 2 || self == 3{
            return true
        }
        
        for i in 2...Int(sqrt(Double(self))) {
            if self % i == 0 {
                return false
            }
        }
        return true
    }
    
    func makeCombination(with count: Int) -> Int {
        let upper: Int = {
            var result = 1
            for n in stride(from: self, through: self - count + 1, by: -1) {
                result *= n
            }
            return result
        }()
        
        let lower: Int = {
            var result = 1
            for n in stride(from: self, through: 1, by: -1) {
                result *= n
            }
            return result
        }()
        
        return upper / lower
    }
}
