# personalrepo
Short Time Fourier Transform

Fourier transform is a method for translating from time domain to frequency domain. But we want to make it one step further using short windowing instead push all the signal onto algorithm. In this case we are using three different windowing methord, which is 

* Barlett, Best for random signal, Good Freqyency Resolution, Fair Spectral Leakage, Fair Amplitude Accuracy
* Blackman, Best for random or mixed signal, Poor Frequency Resolution, Best Spectral Leakage, Good Amplitude Accuracy
* Flat top, Best for sinusoids, Poor Frequency Resolution, Good Spectral Leakage, Best Amplitude Accuracy
* Hanning, Best for random signal, Good Frequency Resolution, Good Spectral Leakage, Fair Amplitude Accuracy
* Hamming, Best for random signal, Good Frequency Resolution, Fair Spectral Leakage, Fair Spectral Leakage
* Kaiser-Bessel, Best for random signal, Fair Frequency Resolution, Good Spectral Leakage, Good Spectral Leakage
* None, Best for transient and synchronous sampling signal, Best Frequency Resolution, Poor Spectral Leakage, Poor Amplitude Accuracy
* Tukey, Best for random signal, Good Frequency Resolution, Poor Spectral Leakage, Poor Amplitude Accuracy
* Welch, Best for random signal, Good Frequency Resolution, Good Spectral Leakage, Fair Amplitude Accuracy