//
//  main.swift
//  LongestPalindrome
//
//  Created by In Taek Cho on 2020-10-18.
//

import Foundation

func solution(_ s:String) -> Int {
    var maximum = 0
    
//    for (index, _) in s.enumerated() {
////        print(index,value)
//        let lenOfFront = s[s.startIndex..<s.index(s.startIndex, offsetBy: index)].count
//        let lenOfBack = s[s.index(s.startIndex, offsetBy: index + 1)...].count
////        print(lenOfFront,lenOfBack)
//        let targetLen = min(lenOfFront, lenOfBack)
//
//        for n in stride(from: targetLen, through: 0, by: -1) {
//            let original = s[s.index(s.startIndex, offsetBy: index - n)...s.index(s.startIndex, offsetBy: index + n)]
////            print(original)
//            if original == String(original.reversed()) {
//                maximum = max(maximum, original.count)
//            }
//        }
//    }
    
    for n in stride(from: s.count, through: 1, by: -1) {
        for startPoint in 0...s.count - n {
            let string = s[s.index(s.startIndex, offsetBy: startPoint)..<s.index(s.index(s.startIndex, offsetBy: startPoint), offsetBy: n)]
//            print(string)
            if string == String(string.reversed()) {
                return string.count
            }
        }
    }
    return maximum
}
