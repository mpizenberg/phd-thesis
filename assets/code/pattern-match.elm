username : User -> Maybe String
username user =
    case user of
        LoggedInWithName name ->
            Just name

        Anonymous ->
            Nothing
