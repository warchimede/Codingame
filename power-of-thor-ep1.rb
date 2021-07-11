STDOUT.sync = true # DO NOT REMOVE
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = gets.split(" ").collect {|x| x.to_i}
tx, ty = initial_tx, initial_ty

# game loop
loop do
    remaining_turns = gets.to_i # The remaining amount of turns Thor can move. Do not remove this line.
    
    # Write an action using puts
    # A single line providing the move to be made: N NE E SE S SW W or NW

    ns = ""
    if light_y > ty
        ns = "S"
        ty += 1
    elsif light_y < ty
        ns = "N"
        ty -= 1
    end

    ew = ""
    if light_x > tx
        ew = "E"
        tx += 1
    elsif light_x < tx
        ew = "W"
        tx -= 1
    end

    puts "#{ns}#{ew}"
end