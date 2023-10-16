import "strings"
func defangIPaddr(address string) string {
    addressArray := strings.Split(address, ".")
    return strings.Join(addressArray, "[.]")
}