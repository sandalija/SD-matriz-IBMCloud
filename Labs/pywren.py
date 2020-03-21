import pywren_ibm_cloud as pywren


def my_map_function(id, x):
    print("I'm activation number {}".format(id))
    return x + 7


if __name__ == "__main__":
    iterdata = [1, 2, 3, 4]
    pw = pywren.ibm_cf_executor()
    pw.map(my_map_function, iterdata)
    print(pw.get_result())
    pw.clean()