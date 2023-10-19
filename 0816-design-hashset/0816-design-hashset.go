import (
    "sort"
    "fmt"
)


type MyHashSet struct {
    elem []int
}


func Constructor() MyHashSet {
    return MyHashSet{
        elem: make([]int, 0, 100),
    }
}


func (this *MyHashSet) Add(key int)  {
    exists := binarySearch(this.elem, key)
    if exists >=0 {
        return
    }
    this.elem = append(this.elem, key)
    sort.Ints(this.elem)
    return
}


func (this *MyHashSet) Remove(key int)  {
    exists := binarySearch(this.elem, key)
    if exists < 0 {
        return
    }

    this.elem = append(this.elem[:exists], this.elem[exists+1:]...)
    return
}


func (this *MyHashSet) Contains(key int) bool {

    exists := binarySearch(this.elem, key)
    if exists >= 0{
        return true
    }
    return false
}

func binarySearch(list []int, key int) int {
	lo := 0
	hi := len(list) - 1

	for lo <= hi {
		mid := (lo + hi) / 2
		if key < list[mid] {
			hi = mid - 1
		} else if key > list[mid] {
			lo = mid + 1
		} else {
            fmt.Println("found ", key, mid)
			return mid
		}
	}
    fmt.Println("didn't find ", key)

	return -1
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Add(key);
 * obj.Remove(key);
 * param_3 := obj.Contains(key);
 */