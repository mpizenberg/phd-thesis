localLetDefinitions : Int
localLetDefinitions =
    let
        x = 14
        y = 42
    -- local definitions with the "let" keyword
    -- are used to resolve the expression
    -- appearing after the mandatory "in" keyword
    in
    x + y


boolToInt : Bool -> Int
boolToInt bool =
    if bool then
        1
    -- if expressions must have an "else" branch.
    -- Both branches must return a value of the same type.
    else
        0

length : List a -> Int
length list =
    -- loops are replaced by higher order functions
    -- transforming an intermediate result step by step.
    List.foldl (\x subtotal -> subtotal + 1) 0 list
