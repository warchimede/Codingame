import Glibc
import Foundation

public struct StderrOutputStream: TextOutputStream {
  public mutating func write(_ string: String) { fputs(string, stderr) }
}
public var errStream = StderrOutputStream()

extension Float {
  var rad: Float { self * .pi / 180 }
}

func toFloat(_ input: String) -> Float {
  Float(input.replacingOccurrences(of: ",", with: "."))!
}

func distance(latA: Float, lonA: Float, latB: Float, lonB: Float) -> Float {
  let x = (lonB - lonA) * cos((latA + latB)/2)
  let y = latB - latA
  return sqrtf(pow(x, 2) + pow(y, 2)) * 6371
}

let lon = toFloat(readLine()!).rad
let lat = toFloat(readLine()!).rad
let n = Int(readLine()!)!
var minDist: Float?
var address: String?
if n > 0 {
  for i in 0...(n-1) {
    var defib = readLine()!.split(separator: ";").map(String.init)
    let latD = toFloat(defib.popLast()!).rad
    let lonD = toFloat(defib.popLast()!).rad
    let dist = distance(latA: lat, lonA: lon, latB: latD, lonB: lonD)
    if minDist == nil || dist < minDist! {
      minDist = dist
      address = defib[1]
    }
  }
}

print(address!)