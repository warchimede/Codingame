import Glibc
import Foundation

public struct StderrOutputStream: TextOutputStream {
  public mutating func write(_ string: String) { fputs(string, stderr) }
}
public var errStream = StderrOutputStream()

let n = Int(readLine()!)! // Number of elements which make up the association table.
let q = Int(readLine()!)! // Number Q of file names to be analyzed.
var mimeDict = [String: String]()
if n > 0 {
  for _ in 0...(n-1) {
    let inputs = (readLine()!).split(separator: " ").map(String.init)
    let ext = inputs[0].lowercased() // file extension
    let mt = inputs[1] // MIME type.
    mimeDict[ext] = mt
  }
}
if q > 0 {
  let unknown = "UNKNOWN"
  for _ in 0...(q-1) {
    let fname = readLine()! // One file name per line.
    let mime = fname.lowercased()
    if !mime.contains(".") {
      print(unknown)
      continue
    }
    let mime2 = mime.split(separator: ".", omittingEmptySubsequences: false)
                    .last
                    .map(String.init)
                    .flatMap { mimeDict[$0] }
    print(mime2 ?? unknown)
  }
}
