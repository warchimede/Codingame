import Glibc
import Foundation

public struct StderrOutputStream: TextOutputStream {
  public mutating func write(_ string: String) { fputs(string, stderr) }
}
public var errStream = StderrOutputStream()

let n = Int(readLine()!)! // the number of temperatures to analyse
var result: String?
var temperature: Int?
for i in ((readLine()!).split(separator: " ").map(String.init)) {
  let t = Int(i)!
    
  if temperature == nil || abs(t) < temperature.map(abs)! || t == temperature.map(abs) {
    temperature = t
    result = i    
  }
}

print("\(result ?? "0")")
