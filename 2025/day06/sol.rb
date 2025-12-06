# AOC 2025 Day 6 – expect input on stdin

ns = $<.readlines
last = ns.pop
$ops = last.split.map(&:to_sym)

def do_sums(a)
    a.zip($ops).map { _1.inject _2 }.sum
end

puts(do_sums ns.map { _1.split.map(&:to_i )}.transpose)          # Part 1

col_widths = last.split(/\*|\+/)[1..].map(&:length)
col_widths[-1] += 1
puts(do_sums ns.map { |l|
    i = 0; col_widths.map { |w| i += w + 1; l.slice(i-w-1, w).chars }
}.transpose.map { _1[0].zip(*_1[1..]).map(&:join).map(&:to_i) }) # Part 2