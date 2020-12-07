import java.io.File

fun calcFuel(mass: Int): Int {
    return mass / 3 - 2
}

fun calcFuel2(mass: Int): Int {
    val fuel = calcFuel(mass)
    if (fuel <= 0) {
        return 0
    }
    return fuel + calcFuel2(fuel)
}

fun main() {
    val masses = File("src/Day01.input").useLines { it.toList() }
    println("Task 1: %d".format(masses.map { calcFuel(it.toInt()) }.sum()))
    println("Task 2: %d".format(masses.map { calcFuel2(it.toInt()) }.sum()))
}
