README:"type [filename].py to begin"

Start menu
    options:
        instructions
        input = instructions
            print instructions
        begin
            input = begin
            BEGIN game

BEGIN game
    text: Black friday at your local Target. Appliances isle
    generate random number from 600-700
    save to list "balance"
    BEGIN MOVEMENT

MOVEMENT
    input = go up or down the isle
            other options: helpme, exit
        start in middle, exit at bottom, expensive appliances at top
    up: go up if exit down
    down: go down if exit down
    take: BEGIN take
    map: BEGIN map
    cart: BEGIN cart
    balance: BEGIN balance
    putBack: begin putBack

HELPME
    print objective + instructions
    end

MAP
    print map of isle (exit at bottom, etc)
    end

TAKE
    INPUT the item you want
    if item in isle
        add to inventory
        delete from isle
    else
        print "invalid item"
    end

CART
    print items in cart
    end

PUTBACK
    input "what would you line to put back?"
    print inventory 
    if item in inventory
        delete from inventory
        add to isle
