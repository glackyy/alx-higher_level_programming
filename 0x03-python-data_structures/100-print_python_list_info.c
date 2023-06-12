#include <Python.h>
void print_python_list_info(PyObject *p)
{
const char *type;
Py_ssize_t i;
Py_ssize_t size = PyList_Size(p);
Py_ssize_t alloc = ((PyListObject *)p)->allocated;
printf("[*] Size of the Python List = %zd\n", size);
printf("[*] Allocated = %zd\n", alloc);
for (i = 0 ; i < size ; i++)
{
PyObject *item = PyList_GetItem(p, i);
*type = Py_TYPE(item)->tp_name;
printf("Element %zd: %s\n", i, type);
}
}
