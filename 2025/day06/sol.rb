# AOC 2025 Day 6 – expect input on stdin

ns = $<.readlines
last = ns.pop
$ops = last.split.map(&:to_sym)

def do_sums(ns) ns.zip($ops).map { _1.inject _2 }.sum end

p do_sums ns.map { _1.split.map(&:to_i ) }.transpose           # Part 1

ws = last.split(/\*|\+/)[1..].map(&:length)
ws[-1] += 1
t = ws.map { |w| "a#{w}" }.join("x")
p do_sums ns.map { _1.unpack(t).map(&:chars) }.transpose.map { # Part 2
    _1.transpose.map(&:join).map(&:to_i) 
}
