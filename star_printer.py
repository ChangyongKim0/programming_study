import logger as lg


class StarPrinter:
    def __init__(self, print_types):
        self.print_queue = [{"type": ele[0], "length": ele[1]}
                            for ele in print_types]
        logger = lg.Logger("StarPrinter")
        self.log, self.err = logger.log, logger.err
        self.log("StarPrinter initialized.")

    def printDiamond(self, length):
        space = "  " * (length // 2)
        star = "*"
        print()
        for line in range(length):
            print(space + star)
            if line < length / 2 - 1:
                space = space[0:-2]
                star += "****"
            else:
                space += "  "
                star = star[0:-4]
        print()

    def printTriangle(self, length):
        space = " " * length
        star = "*"
        print()
        for line in range(length):
            print(space + star)
            space = space[0:-1]
            star += "**"
        print()

    def printLeftTriangle(self, length):
        star = "*"
        print()
        for line in range(length):
            print(star)
            star += "**"
        print()

    def addPrintQueue(self, print_type, length):
        self.print_queue.append({"type": print_type, "length": length})
        self.log("{} with length {} is added in print queue.".format(
            print_type, length))

    def printStar(self):
        for ele in self.print_queue:
            if ele["type"] == "diamond":
                self.printDiamond(ele["length"])
            elif ele["type"] == "triangle":
                self.printTriangle(ele["length"])
            elif ele["type"] == "left_triangle":
                self.printLeftTriangle(ele["length"])
            else:
                self.err("Wrong print type.")

    def __str__(self):
        string = "<StarPrinter>\n[print_queue]\n"
        for ele in self.print_queue:
            string += "type: {0}; length: {1}\n".format(
                ele["type"], ele["length"])
        return string


if __name__ == "__main__":
    star_printer = StarPrinter([["triangle", 5], ["left_triangle", 3]])
    print(star_printer)
    star_printer.addPrintQueue("none", 8)
    star_printer.addPrintQueue("diamond", 7)
    print(star_printer)
    star_printer.printStar()
