#%%
# https://www.tutorialspoint.com/tensorflow/tensorflow_quick_guide.htm
# https://www.tensorflow.org/tutorials/customization/basics
import numpy as np
import tensorflow as tf


#%%
# Dimensies van tensors of matrikse
tensor_1d = np.array([1.3, 1, 4.0, 23.99])
print(tensor_1d)

#%%
print(tensor_1d[0])

print(tensor_1d[2])

# %%
tensor_2d = np.array([(1,2,3,4),(4,5,6,7),(8,9,10,11),(12,13,14,15)])

print(tensor_2d)
tensor_2d[3][2]
# %%
# Tensor berekeninge en hantering
matrix1 = np.array([(2,2,2),(2,2,2),(2,2,2)],dtype = 'int32')
matrix2 = np.array([(1,1,1),(1,1,1),(1,1,1)],dtype = 'int32')

print (matrix1)
print (matrix2)

# %%
matrix1 = tf.constant(matrix1)
print(matrix1)
matrix2 = tf.constant(matrix2)
print(matrix2)
matrix_product = tf.matmul(matrix1, matrix2)
print(matrix_product)
matrix_sum = tf.add(matrix1,matrix2)
print(matrix_sum)
matrix_3 = np.array([(2,7,2),(1,4,2),(9,0,2)],dtype = 'float32')
print (matrix_3)
matrix_det = tf.linalg.det(matrix_3)

print(matrix_det)
#%%
print(tf.math.add(1, 2))
print(tf.math.add([1, 2], [3, 4]))
print(tf.math.square(5))
print(tf.math.reduce_sum([1, 2, 3]))

# Operator overloading is also supported
print(tf.math.square(2) + tf.math.square(3))
# %%
x = tf.linalg.matmul([[1]], [[2, 3]])
print(x)
print(x.shape)
print(x.dtype)
# %%
# Convert between tensors and numpy arrays
ndarray = np.ones([3, 3])

print("TensorFlow operations convert numpy arrays to Tensors automatically")
tensor = tf.math.multiply(ndarray, 42)
print(tensor)


print("And NumPy operations convert Tensors to NumPy arrays automatically")
print(np.add(tensor, 1))

print("The .numpy() method explicitly converts a Tensor to a numpy array")
print(tensor.numpy())

# %%
x = tf.random.uniform([3, 3])

print("Is there a GPU available: "),
print(tf.config.list_physical_devices("GPU"))

print("Is the Tensor on GPU #0:  "),
print(x.device.endswith('GPU:0'))
# %%
