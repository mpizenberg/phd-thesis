missing patterns
Line 20, Column 5
This `case` does not have branches for all possibilities:

20|>    case user of
21|>        LoggedinWithName name ->
22|>            Just name

Missing possibilities include:

    Anonymous

I would have to crash if I saw one of those. Add branches for them!

Hint: If you want to write the code for each branch later, use `Debug.todo` as a
placeholder. Read <https://elm-lang.org/0.19.0/missing-patterns> for more
guidance on this workflow.
