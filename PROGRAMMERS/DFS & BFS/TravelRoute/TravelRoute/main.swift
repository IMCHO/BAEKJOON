//
//  main.swift
//  TravelRoute
//
//  Created by In Taek Cho on 2020-09-25.
//

import Foundation

func solution(_ tickets:[[String]]) -> [String] {
    var infos = [String:[String]]()
    
    for ticket in tickets {
        if var info = infos[ticket[0]] {
            info.append(ticket[1])
            info.sort()
            infos[ticket[0]] = info
        } else {
            infos[ticket[0]] = [ticket[1]]
        }
    }
    
    var stack = ["ICN"]
    var result = [String]()

    
    while stack.count != 0 {
        guard let now = stack.last else {
            return []
        }
        
        if !infos.keys.contains(now) || infos[now]?.count == 0 {
            result.append(stack.removeLast())
        } else {
            guard let next = infos[now]?.removeFirst() else {
                return []
            }
            stack.append(next)
        }
    }
    
    return result.reversed()
}

//let test = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
//print(solution(test))
