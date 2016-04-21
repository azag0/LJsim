from cffi import FFI


ffi = FFI()
with open('lj_func.h') as f:
    src = f.read()
ffi.set_source('_lj_func', src, libraries=['lj'], library_dirs=['.'])
ffi.cdef(src + """

extern "Python" void inv(double *A, double *A_inv, int n);""")
ffi.compile()
