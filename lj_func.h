struct Sp_t {
    double eps, sigma, rc, L, dt;
    int N, Nt, thermo, seed;
    _Bool dump, use_numba, use_cython, use_fortran, use_cfortran,
          use_cffi;
};

double tot_pe(double *pos_list, struct Sp_t sp, int n);

void force_list(double *pos_list,
                struct Sp_t sp,
                void (*inv)(double *A_in, double *A_out, int n),
                double *F,
                int n);
