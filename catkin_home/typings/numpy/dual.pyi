"""
This type stub file was generated by pyright.
"""

import numpy.linalg as linpkg
import numpy.fft as fftpkg

"""
Aliases for functions which may be accelerated by Scipy.

Scipy_ can be built to use accelerated or otherwise improved libraries
for FFTs, linear algebra, and special functions. This module allows
developers to transparently support these accelerated functions when
scipy is available but still support users who have only installed
NumPy.

.. _Scipy : https://www.scipy.org

"""
fft = fftpkg.fft
ifft = fftpkg.ifft
fftn = fftpkg.fftn
ifftn = fftpkg.ifftn
fft2 = fftpkg.fft2
ifft2 = fftpkg.ifft2
norm = linpkg.norm
inv = linpkg.inv
svd = linpkg.svd
solve = linpkg.solve
det = linpkg.det
eig = linpkg.eig
eigvals = linpkg.eigvals
eigh = linpkg.eigh
eigvalsh = linpkg.eigvalsh
lstsq = linpkg.lstsq
pinv = linpkg.pinv
cholesky = linpkg.cholesky
_restore_dict = {  }
def register_func(name, func):
    ...

def restore_func(name):
    ...

def restore_all():
    ...
