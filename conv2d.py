import numpy as np


def conv_2d(x, kernel, bias, P):
    # .shape komutu mxn boyutundaki kernel matrisinin boyutlarını int olarak verir. 0 > m, 1 > n bileşenini verir.
    kernel_shape = kernel.shape[0]
    xnew_shape= x.shape[0] + (2 * P)
    
    if P > 0 :
        xnew = np.zeros((xnew_shape , xnew_shape))
        xnew [P:xnew.shape[0]-P, P:xnew.shape[1]-P] = x
            
    else:
      xnew = x
    
    output_shape = xnew.shape[0] - kernel_shape + 1 
    result = np.zeros((output_shape, output_shape))
    
    for row in range(xnew.shape[0] - 1):
            for col in range(xnew.shape[1] - 1):
                window = xnew[row: row + kernel_shape, col: col + kernel_shape]
                result[row, col] = np.sum(np.multiply(kernel,window))
    return result + bias

        

#n>f için (n x n) bir matris ile (f x f) bir matrisin konvolüsyonunun sonucunda elde edilen matrisin boyutları
# ((n - f + 1 ) x (n - f + 1 )) şeklinde olur. Aşağıdaki örnekte 3x3 bir matris ile 2x2 bir matris işleme sokuluyor. 
# Sonuç olarak 2x2 bir matris elde ediliyor.
# Padding
# Köşelerdeki piksellerin sisteme daha fazla dahil olması için, matrisin etrafını 0 lar ile kaplama yöntemi.
# Konvolüsyon sonucu elde edilen matrisin boyutu K = n+2*P-f+1 ===> K x K boyutunda olur.
    


























