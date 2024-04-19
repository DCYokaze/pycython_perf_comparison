import sol01_pure_python
import sol01_pure_python_cy
import sol01_pure_python_cy_cpdef
import sol01_pure_python_cypp_cpdef
import sol01_numpy
import sol01_pure_python_cypp_cpdef_wolist
import pytest
import time
import numpy

# d = [0]*(10**8)
# sol01_pure_python_cy.count_increases(d)

@pytest.mark.benchmark(
    group="group-name",
    min_time=0.1,
    max_time=0.5,
    min_rounds=15,
    timer=time.time,
    disable_gc=True,
    warmup=False
)

@pytest.mark.parametrize("n", [10**2, 10**4])
def test_count_increases_pure_python(benchmark,n):
  d = [0]*(n)
  result = benchmark(sol01_pure_python.count_increases,d )
  
@pytest.mark.parametrize("n", [10**2, 10**4])
def test_count_increases_cy_01(benchmark,n):
  d = [0]*(n)
  result = benchmark(sol01_pure_python_cy.count_increases,d )

@pytest.mark.parametrize("n", [10**2, 10**4])
def test_count_increases_cy_cpdef(benchmark,n):
  d = [0]*(n)
  result = benchmark(sol01_pure_python_cy_cpdef.count_increases_cy,d )

@pytest.mark.parametrize("n", [10**2, 10**4])
def test_count_increases_cypp_cpdef(benchmark,n):
  d = [0]*(n)
  result = benchmark(sol01_pure_python_cypp_cpdef.count_increases_cpp,d )

@pytest.mark.parametrize("n", [10**2, 10**4])
def test_count_increases_cypp_cpdef_wolist(benchmark,n):
  d = [0]*(n)
  result = benchmark(sol01_pure_python_cypp_cpdef_wolist.count_increases_cpp,d )

@pytest.mark.parametrize("n", [10**2, 10**4])
def test_count_increases_cy_numpy(benchmark,n):
  d = [0]*(n)
  # bytes_object = bytes(d)
  arr = numpy.array(d)
  result = benchmark(sol01_numpy.count_increases_cy_array,arr )

# @pytest.mark.parametrize("n", [1, 10**2, 10**4])
# def test_remove_from_list_first(benchmark,n):
#   result = benchmark(remove_from_list_first,n )
  
# def remove_from_list_last(n=10**4):
#   aList = [0]*n
#   for i in reversed(range(n)):
#     aList.pop(-1)

# def remove_from_list_first(n=10**4):
#   aList = [0]*n
#   for i in range(n):
#     aList.pop(0)


if __name__ == "__main__":
  print("in __main__")
  pytest.main()
  # remove_from_list_last(10**2)
  # test_f1()
  pass
  # main()