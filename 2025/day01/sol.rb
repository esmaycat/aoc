p1 = p2 = 0
d = 50
puts($<.each_line.map{ _1.tr('RL', '+-').to_i }.map { |r|
    z = d == 0 ? 1 : 0
    s, d = (d + r).divmod 100
    s = s.abs
    s += d == 0 ? 1 : 0 - z if r < 0
    [d == 0 ? 1 : 0, s]
}.transpose.map(&:sum))
