import Glibc
import Foundation

public struct StderrOutputStream: TextOutputStream {
  public mutating func write(_ string: String) { fputs(string, stderr) }
}
public var errStream = StderrOutputStream()

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 * ---
 * Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.
 **/

let inputs = (readLine()!).split(separator: " ").map(String.init)
let lightX = Int(inputs[0])! // the X position of the light of power
let lightY = Int(inputs[1])! // the Y position of the light of power
var tx = Int(inputs[2])! // Thor's starting X position
var ty = Int(inputs[3])! // Thor's starting Y position

// game loop
while true {
  let remainingTurns = Int(readLine()!)! // The remaining amount of turns Thor can move. Do not remove this line.

  var ns = ""
  if ty < lightY {
    ns = "S"
    ty += 1
  } else if ty > lightY {
    ns = "N"
    ty = ty - 1
  }

  var ew = ""
  if tx < lightX {
    ew = "E"
    tx += 1
  } else if tx > lightX {
    ew = "W"
    tx = tx - 1
  }

  // A single line providing the move to be made: N NE E SE S SW W or NW
  print("\(ns)\(ew)")
}
