type Msg
    = WindowResizes Device.Size
      -- pointer events
    | PointerMsg Pointer.Msg
      -- select things
    | SelectImage Int
    | SelectTool Int
    | SelectClass Int
      -- files
    | LoadImages (List { name : String, file : Value })
    | ImageLoaded { id : Int, url : String, width : Int, height : Int }
    | LoadConfig Value
    | ConfigLoaded String
    | Export
      -- other actions
    | ZoomMsg ZoomMsg
    | RemoveLatestAnnotation
