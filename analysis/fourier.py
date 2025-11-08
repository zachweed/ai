import numpy as np

class Fourier:
  def fourier_plot_for(cls, l, n, a, b, f, dx):
    x = np.linspace(-L, L, N, endpoint = False)

    # actual fourier transform
    fourier = fft(f)
    fourier = fftshift(fourier)
    fourier *= dx

    # defines frequency
    frequency = fftfreq(N, d=dx)
    frequency = fftshift(frequency)
    k = 2 * np.pi * frequency

    # Real, imaginary, and absolute
    # aspects of F(k)
    F_real = np.real(fourier)
    F_imag = np.imag(fourier)
    F_abs = np.abs(fourier)

    # Plotting
    figure, axis = plt.subplots(3, 1, figsize = (7, 8), sharex = True)

    # Real
    axis[0].plot(k, F_real)
    axis[0].set_ylabel("Re[F(k)]")
    axis[0].grid(True)

    # Imaginary
    axis[1].plot(k, F_imag)
    axis[1].set_ylabel("Im[F(k)]")
    axis[1].grid(True)

    # Absolute
    axis[2].plot(k, F_abs)
    axis[2].set_ylabel("|F(k)|")
    axis[2].set_xlabel("k (angular frequency)")
    axis[2].grid(True)

    plt.tight_layout()
    plt.show()