import "strings"
func finalValueAfterOperations(operations []string) int {
    x:=0
    for _, v := range operations{
        if strings.Contains(v, "-"){
            x--
        }else {
            x++
        }
    }

    return x
}