ps = $<.to_a(chomp: true).map { _1.split(',').map(&:to_i) }
def area(p1, p2)
  (p1[0] - p2[0] + 1).abs * (p1[1] - p2[1] + 1).abs
end
p ps.combination(2).map { area _1, _2 }.max

xs = ps.map(&:first).uniq.sort
ys = ps.map(&:last).uniq.sort
x_map = xs.each_with_index.to_h
y_map = ys.each_with_index.to_h

width, height = xs.length, ys.length 
grid = Array.new(height) { Array.new(width, ' ') }
ps.each { |(x, y)| grid[y_map[y]][x_map[x]] = 'R' }
(ps + [ps.first]).each_cons(2) { |(x1, y1), (x2, y2)|
  x1, y1 = x_map[x1], y_map[y1]
  x2, y2 = x_map[x2], y_map[y2]
  if x1 == x2
    dy = y1 < y2 ? 1 : -1
    grid[y1 += dy][x1] = 'G' until y1 == y2 - dy
  else
    dx = x1 < x2 ? 1 : -1
    grid[y1][x1 += dx] = 'G' until x1 == x2 - dx
  end
}

q = [[0, 0]]
grid[0][0] = '.'
until q.empty?
  x, y = q.shift
  grid[y][x] = '#'
  [[0, 1], [0, -1], [1, 0], [-1, 0]].each { |(dx, dy)|
    nx, ny = (x + dx) % width, (y + dy) % height
    if grid[ny][nx] == ' '
      grid[ny][nx] = '.'
      q << [nx, ny]
    end
  }
end

grid.map{puts _1.join}

part2 = 0
ps.combination(2).filter_map { |p1, p2|
  a = area p1, p2
  next if a < part2
  x1, x2 = [x_map[p1[0]], x_map[p2[0]]].sort
  y1, y2 = [y_map[p1[1]], y_map[p2[1]]].sort
  #p("#{p1}, #{p2}, #{a} #{(x1..x2).to_a.product((y1..y2).to_a).all? { |(x, y)| grid[y][x] != '#'}}")
  part2 = [a, part2].max if (x1..x2).to_a.product((y1..y2).to_a).all? { |(x, y)| grid[y][x] != '#'}
}.max

p(part2)
