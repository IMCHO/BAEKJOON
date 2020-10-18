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
    
//    for n in stride(from: s.count, through: 1, by: -1) {
//        for startPoint in 0...s.count - n {
//            let string = s[s.index(s.startIndex, offsetBy: startPoint)..<s.index(s.index(s.startIndex, offsetBy: startPoint), offsetBy: n)]
////            print(string)
////            if string == String(string.reversed()) {
////                return string.count
////            }
////            for index in 0...Int(string.count / 2) {
////                if string[string.index(string.startIndex, offsetBy: index)] != string[string.index(string.startIndex, offsetBy: string.count - index - 1)] {
////                    break
////                }
////                if index == Int(string.count / 2) {
////                    return string.count
////                }
////            }
//
//            let arrOfString = string.map { $0 }
//            var left = 0
//            var right = string.count - 1
//
//            while left <= right && arrOfString[left] == arrOfString[right] {
//                left += 1
//                right -= 1
//            }
//
//            if left > right { return string.count }
//        }
//    }
    
    let arrOfS = s.map { $0 }
    
    for start in 0..<arrOfS.count {
        for end in stride(from: arrOfS.count - start - 1, through: maximum, by: -1) {
            var left = start
            var right = start + end
            
            while left <= right && arrOfS[left] == arrOfS[right] {
                left += 1
                right -= 1
            }
            
            if left > right { maximum = max(maximum, end + 1) }
        }
    }
    return maximum
}

print(solution("abcdcba"))
print(solution("abacde"))
