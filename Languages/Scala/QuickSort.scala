// Source: ChatGPT

object QuickSort {
  
  var LOGGING: Boolean = false
  
  def sort(arr: Array[Int], low: Int, high: Int): Unit = {
    if (low < high) {
      val pivot = partition(arr, low, high)
      sort(arr, low, pivot-1)
      sort(arr, pivot+1, high)
    }
  }

  def partition(arr: Array[Int], low: Int, high: Int): Int = {
    val pivot = arr(high)
    var i = low - 1
    for (j <- low until high) {
      if (arr(j) < pivot) {
        i += 1
        val temp = arr(i)
        arr(i) = arr(j)
        arr(j) = temp
      }
    }
    val temp = arr(i+1)
    arr(i+1) = arr(high)
    arr(high) = temp
    i+1
  }

  def main(args: Array[String]): Unit = {
    val arr = Array(10650,56341,77676,47158,34999,22009,19680,41870,31090,30668)
    sort(arr, 0, arr.length-1)
    if (QuickSort.LOGGING) {
      println("Sorted array:")
      for (i <- arr.indices) {
        print(arr(i) + " ")
      }
    }
  }
}