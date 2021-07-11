STDOUT.sync = true # DO NOT REMOVE
# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.

# game loop
loop do
    index = 0
    height = 0
    8.times do |i|
        mountain_h = gets.to_i # represents the height of one mountain.
        if mountain_h > height
            height = mountain_h
            index = i
        end
    end
        
    puts index # the index of the mountain to fire on.
end