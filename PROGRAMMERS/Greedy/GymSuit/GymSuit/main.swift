//
//  main.swift
//  GymSuit
//
//  Created by In Taek Cho on 2020-09-26.
//

import Foundation

func solution(_ n:Int, _ lost:[Int], _ reserve:[Int]) -> Int {
    var copiedReserve = Set(reserve).subtracting(Set(lost))
    var copiedLost = Set(lost).subtracting(Set(reserve))
    
    var cnt = 0
//    for l in copiedLost {
//        if copiedReserve.contains(l - 1) {
//            copiedReserve.remove(at: copiedReserve.firstIndex(where: { $0 == l - 1 })!)
//            cnt += 1
//        } else if copiedReserve.contains(l + 1) {
//            copiedReserve.remove(at: copiedReserve.firstIndex(where: { $0 == l + 1 })!)
//            cnt += 1
//        }
//    }
    
    for c in copiedReserve {
        if copiedLost.contains(c - 1) {
            copiedLost.remove(at: copiedLost.firstIndex(where: { $0 == c - 1 })!)
        } else if copiedLost.contains(c + 1) {
            copiedLost.remove(at: copiedLost.firstIndex(where: { $0 == c + 1 })!)
        }
    }

    return n - (copiedLost.count - cnt)
}
