#include <Python.h>

static PyObject *method_fputs(PyObject *self, PyObject *args) {

    char *str, *filename = NULL;
    int copied_bytes = -1;

    /*
     * Parse args from Python to C 
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
