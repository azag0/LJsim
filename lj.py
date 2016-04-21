from _lj_func import ffi, lib
import numpy as np


@ffi.def_extern()
def inv(A, A_inv, n):
    A = np.ndarray(shape=(n, n), buffer=ffi.buffer(A, (n**2)*8))
    A_inv = np.ndarray(shape=(n, n), buffer=ffi.buffer(A_inv, (n**2)*8))
    A_inv[:] = np.linalg.inv(A)


def tot_PE(pos_list, sp):
    return lib.tot_pe(ffi.cast('double *', np.asfortranarray(pos_list).ctypes.data),
                      sp,
                      pos_list.shape[0])


def force_list(pos_list, sp):
    F = np.zeros_like(pos_list, order='F')
    lib.force_list(ffi.cast('double *', np.asfortranarray(pos_list).ctypes.data),
                   sp,
                   lib.inv,
                   ffi.cast('double *', F.ctypes.data),
                   pos_list.shape[0])
    return F
