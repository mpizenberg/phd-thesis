module Main exposing (..)

import Element as El exposing (Color, Element)
import Element.Background as Background

main = El.layout [] content

content : Element msg
content =
    El.column [ El.height El.fill, El.width El.fill ]
        [ header
        , centeredText
        ]

header : Element msg
header =
    El.row [ El.width El.fill ]
        [ El.el [ El.alignLeft ] (rectangle (El.rgb 1 0.5 0.5) "red")
        , El.el [ El.alignLeft ] (rectangle (El.rgb 0.5 1 0.5) "green")
        , El.el [ El.alignRight ] (rectangle (El.rgb 0.5 0.5 1) "blue")
        ]

rectangle : Color -> String -> Element msg
rectangle color text =
    El.el
        [ Background.color color
        , El.height (El.px 50)
        , El.width (El.px 100)
        ]
        (El.text text)

centeredText : Element msg
centeredText =
    El.el [ El.centerY, El.centerX ]
        (El.text "This text is vertically and horizontally centered!")
