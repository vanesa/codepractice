package main
	
import "fmt"

func main() {
	var noun string
	var verb string
	var adjective string
	var noun2 string

	fmt.Println("Mad lib program!")
	
	fmt.Println("Give me a noun!: ")
	fmt.Scanln(&noun)

	fmt.Println("Give me a verb!: ")
	fmt.Scanln(&verb)	

	fmt.Println("Give me a adjective!: ")
	fmt.Scanln(&adjective)

	fmt.Println("Give me a noun!: ")
	fmt.Scanln(&noun2)

	fmt.Println(fmt.Sprintf("The %v %v to the %v %v", noun, verb, adjective, noun2))
	
	}

