-- Definition of type Bool as a custom type with two variants
type Bool
    = False
    | True

-- Custom type with one variant
type Unit
    = Unit

-- Custom type with three variants holding other types
type OneOfThreeBools
    = First Bool
    | Second Bool
    | Third Bool

-- Custom type holding data of a generic type (lower case)
type Container a
    = Container a

-- Definition of a generic linked list with a custom recursive type
type List a
    = EmptyList
    | AtLeastOne a (List a)
