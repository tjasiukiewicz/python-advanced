#include <Python.h>

static PyObject *method_fputs(PyObject *self, PyObject *args) {

    char *str, *filename = NULL;
    int copied_bytes = -1;

    /*
     * Parse args from python to C 
     * format: https://docs.python.org/3/c-api/arg.html
     */
    if(!PyArg_ParseTuple(args, "ss", &str, &filename)) {
        return NULL;
    }

    FILE *fp = fopen(filename, "w");

    copied_bytes = fputs(str, fp);

    fclose(fp);

    /* Return copied_bytest to Python */
    return PyLong_FromLong(copied_bytes);
}

/* METH_VARARGS - accept args type PyObject**: self, args */
/* https://docs.python.org/3/c-api/structures.html */
static PyMethodDef FputsMethods[] = {
    {"fputs", method_fputs, METH_VARARGS, "Python interface to fputs C library function"},
    {NULL, NULL, 0, NULL}
};

/* 
 * -1: dosen't have support for subinterpreters
 * non-negative: re-initialization module, memory alloc on each subinterpreter
 */
static struct PyModuleDef fputsmodule = {
    PyModuleDef_HEAD_INIT,
    "fputs",
    "Python interface to fputs C library function",
    -1,
    FputsMethods
};

/*
 * init module
 */
PyMODINIT_FUNC PyInit_fputs(void) {
    return PyModule_Create(&fputsmodule);
}

