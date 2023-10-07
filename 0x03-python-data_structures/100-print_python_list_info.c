#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - Prints python list info
 * @p: Python object
 */
void print_python_list_info(PyObject *p)
{
        int size, space, index;
        PyObject *obj;
        size = Py_SIZE(p);
        space = ((PyListObject *)p)->allocated;
        printf("[*] Size of the Python List = %d\n", size);
        printf("[*] Allocated = %d\n", space);
        for (index = 0; index < size; index++)
        {
                printf("Element %d: ", index);
                obj = PyList_GetItem(p, index);
                printf("%s\n", Py_TYPE(obj)->tp_name);
        }
}
