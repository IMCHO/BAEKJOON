//
//  main.swift
//  TravelRoute
//
//  Created by In Taek Cho on 2020-09-25.
//

import Foundation

func solution(_ tickets:[[String]]) -> [String] {
    var infos = [String:[String]]()
    var copiedTickets = tickets
    
    for ticket in tickets {
        if var info = infos[ticket[0]] {
            info.append(ticket[1])
            info.sort()
            infos[ticket[0]] = info
        } else {
            infos[ticket[0]] = [ticket[1]]
        }
    }
    
    var stack = [["ICN":["ICN"]]]

    
    while true {
        let start = stack.removeLast()
        
    }
    
    return []
}

let test = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
print(solution(test))
