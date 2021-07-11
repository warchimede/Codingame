import Glibc
import Foundation

public struct StderrOutputStream: TextOutputStream {
  public mutating func write(_ string: String) { fputs(string, stderr) }
}
public var errStream = StderrOutputStream()

// game loop
while true {
  var index = 0
  var height = 0
  
  for i in 0...7 {
    let mountainH = Int(readLine()!)! // represents the height of one mountain.
      
    if mountainH > height {
      height = mountainH
      index = i
    }
  }

  print(index);     // The index of the mountain to fire on.
}
