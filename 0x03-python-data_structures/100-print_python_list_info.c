#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
#include <listobject.h>

/**
 * print_python_list_info - prints basic info about Python lists. 
 * @p: Pyobject.
 */
void print_python_list_info(PyObject *p)
{
	int i;

	printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < Py_SIZE(p); i++)
	{
		printf("Element %d: %s\n", i);
		printf("%s\n", Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
}
