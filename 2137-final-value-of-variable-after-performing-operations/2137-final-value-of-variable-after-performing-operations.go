
func finalValueAfterOperations(operations []string) int {
    x:=0
    for _, v := range operations{
        r := []rune(v)
        if r[0]=='-' || r[len(r)-1] == '-'{
            x--
            continue
        }
            x++
    }

    return x
}