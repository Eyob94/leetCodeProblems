func finalValueAfterOperations(operations []string) int {
    	x := 0
	for _, val := range operations {
		lenStr := utf8.RuneCountInString(val)
		if string(val[0]) == "-" || string(val[lenStr-1]) == "-" {
			x--
			continue
		}
		x++
	}
	return x
}