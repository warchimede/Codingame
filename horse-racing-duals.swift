import Glibc
import Foundation

public struct StderrOutputStream: TextOutputStream {
  public mutating func write(_ string: String) { fputs(string, stderr) }
}
public var errStream = StderrOutputStream()

var result = 10000000
var powers = [Int]()
let N = Int(readLine()!)!
if N > 0 {
  for _ in 0...(N-1) {
    powers.append(Int(readLine()!)!)
  }
}
powers.sort()
for i in 1..<powers.count {
  let diff = powers[i] - powers[i - 1]
  result = diff < result ? diff : result
}
print(result)