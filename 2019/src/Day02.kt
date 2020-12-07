import java.io.File


fun step(data: IntArray, pos: Int): IntArray {
    val opcode = data[pos]
    if (opcode == 1) {
        val x = data[data[pos+1]]
        val y = data[data[pos+2]]
        val z = x + y
        data[data[pos+3]] = z
        println("%d + %d = %d".format(x, y, z))
    }
    if (opcode == 2) {
        val x = data[data[pos+1]]
        val y = data[data[pos+2]]
        val z = x * y
        data[data[pos+3]] = z
        println("%d * %d = %d".format(x, y, z))
    }
    return data
}


fun main() {

    var intcodes = File("src/Day02.input").readText().split(",").map { it.toInt() }.toIntArray()

    println(intcodes.size)

    intcodes[1] = 12
    intcodes[2] = 2

    for (i in intcodes.indices step 4) {
        println(i)
        if (intcodes[i] == 99) {
            println("BREAK")
            break;
        }
        println(intcodes.toList())
        intcodes = step(intcodes, i)
    }

    println("Day 2 Task 1: %d".format(0))
}
