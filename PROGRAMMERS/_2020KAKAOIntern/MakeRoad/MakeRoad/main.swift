//
//  main.swift
//  MakeRoad
//
//  Created by In Taek Cho on 2020-10-09.
//

import Foundation

func solution(_ board:[[Int]]) -> Int {
    return min(BFS(with: [0,0,0,0], and: board), BFS(with: [0,0,2,0], and: board))
}

func checkArea(with pos: [Int], and board: [[Int]]) -> Bool {
    if pos[0] >= 0 && pos[0] < board.count && pos[1] >= 0 && pos[1] < board.count && board[pos[0]][pos[1]] == 0 {
        return true
    } else {
        return false
    }
}

func BFS(with start: [Int], and board: [[Int]]) -> Int {
    var queue = [start]
    let len = board.count
    var visitInfo = Array(repeating: Array(repeating: 0, count: len), count: len)
    let offsets = [[1,0,0], [-1,0,1], [0,1,2], [0,-1,3]]
    var minimum = Int.max
    visitInfo[0][0] = 1

    while queue.count != 0 {
        let nowInfo = queue.removeFirst()
        let nowX = nowInfo[0]
        let nowY = nowInfo[1]
        let nowDir = nowInfo[2]
        let nowCost = nowInfo[3]
        
        if nowX == len - 1 && nowY == len - 1 {
            minimum = min(minimum, nowCost)
//            print(visitInfo)
            continue
        }
        
        for offset in offsets {
            var newInfo = [Int]()
            if nowDir == offset[2] {
                newInfo = [nowX + offset[0], nowY + offset[1], nowDir, nowCost + 100]
            } else {
                newInfo = [nowX + offset[0], nowY + offset[1], offset[2], nowCost + 600]
            }
            if !checkArea(with: [newInfo[0], newInfo[1]], and: board) { continue }
            if visitInfo[newInfo[0]][newInfo[1]] == 0 || visitInfo[newInfo[0]][newInfo[1]] >= newInfo[3] {
                visitInfo[newInfo[0]][newInfo[1]] = newInfo[3]
                queue.append(newInfo)
            }
        }
    }
    
    return minimum
}

print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
