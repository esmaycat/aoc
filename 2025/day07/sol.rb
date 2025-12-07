lines = $<.readlines
beams = { lines.first.index("S") => 1 }
beams.default = 0

p1 = 0
lines.each { |l|
  next unless l.include? "^"
  l.length.times.select { l[_1] == "^" }.each { |s|
    p1 += 1 if beams[s] > 0
    beams[s + 1] += beams[s]
    beams[s - 1] += beams[s]
    beams[s] = 0
  }
}

p p1
p beams.each_value.sum
