def auto_correlation(type, data):
    """Doing correlation to the signal itself using designed mathematics equation. Time shifted to the length of data.

    Parameters
    ----------
    type : String
        Function type: normal for using the direct correlation, inversefourier using magnitude spectrum
    data : 1D array
        Input of the function, data signal

    Returns
    -------
    1D array
        Return of the autocorrelation
    """
    
    from numpy import array, zeros, correlate, exp, pi
    
    result = array(zeros(len(data)), dtype=complex)
    magnitude_spectrum = array(zeros(len(data)), dtype=complex)
    if type == "normal":
        return [x/len(data) for x in correlate(data, data, mode="same")]
    elif type == "inversefourier":
        for i in range(len(data)):
            for j in range(len(data)):
                magnitude_spectrum[i] += (data[j]**2)*exp(-2j*pi*i*j/len(data))
        
        for i in range(len(data)):
            for j in range(len(data)):
                result[i] += (magnitude_spectrum[j]**2)*exp(2j*pi*i*j/len(magnitude_spectrum))
            result[i] = result[i]/len(magnitude_spectrum)
        return result
    else: raise Exception("Please check the available type!") 
  
    
def cross_correlation(type, first_data, second_data):
    """Doing correlation on two signal using designed mathematical equation. Time shifted to the first signal. 

    Parameters
    ----------
    type : String
        Function type: normal for using the direct correlation, inversefourier using magnitude spectrum
    firstdata : 1D Array
        Base signal for correlation. The signal that doesn't move on the line.
    seconddata : 1D Array
        Signal for the correlation, signal move across the first signal.

    Returns
    -------
    1D Array
        Return of the function with length of the first signal.
    """
    
    from numpy import correlate, sqrt

    if len(first_data) != len(second_data):
        raise Exception("Please select the same length of the first and second data!")

    data_length = len(first_data)

    if type == "normal":
        return [x/data_length for x in correlate(first_data, second_data, mode="same")]
    elif type == "normalnormalized":
        rxy = [x/data_length for x in correlate(first_data, second_data, mode="same")]
        rxx = auto_correlation("normal", first_data)
        ryy = auto_correlation("normal", second_data)
        return rxy/(sqrt(rxx)*sqrt(ryy))
    

def ecg_peak_finding(type, data):
    """Finding the peak position of the electrocardiogram signal based on the correlation mathematical function method.

    Parameters
    ----------
    type : String
        Function type: normal for using the direct correlation, inversefourier using magnitude spectrum
    data : 1D Array
        Input array of electrocardiogram signal

    Returns
    -------
    Tuple [1D Array, 1D Array]
        Return the peak position and the peak value of the electrocardiogram signal.
    """
    
    from scipy.signal import find_peaks
    
    correlation = auto_correlation(type, data)
    peak_position = find_peaks(correlation, distance=100, height=0.1)[0]

    peak_value = [correlation[i] for i in peak_position]
    return peak_position, peak_value