//
//  main.swift
//  SkillTree
//
//  Created by In Taek Cho on 2020-10-28.
//

import Foundation

func solution(_ skill:String, _ skill_trees:[String]) -> Int {
    var skillDict = [String:Int]()
    for (index, s) in skill.enumerated() {
        skillDict[String(s)] = index
    }
    var result = 0
    
    for skillTree in skill_trees {
        var status = Array(repeating: false, count: skillDict.count)
        var isCompleted = true
        
        for c in skillTree {
            if let index = skillDict[String(c)] {
                if index == 0 {
                    status[index] = true
                } else {
                    let beforeSkills = status[0...index - 1].filter({ $0 == false })
                    if beforeSkills.count == 0 {
                        status[index] = true
                    } else {
                        isCompleted = false
                        break
                    }
                }
            }
        }
        
        if isCompleted {
            result += 1
        }
    }
    
    
    return result
}
