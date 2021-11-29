import star_printer as sp

star_printer = sp.StarPrinter([["triangle", 5], ["left_triangle", 3]])
print(star_printer)
star_printer.addPrintQueue("notype", 8)
star_printer.addPrintQueue("diamond", 7)
print(star_printer)
star_printer.printStar()
