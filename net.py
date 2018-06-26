from numpy import exp, array, random, dot
inputs=array([[1,0],[0,1],[0,0]])
outputs=array([[1,1,0]]).T
random.seed(1)
weights=2*random.random((2,1))-1
for i in range(10000):
	output=1/(1+exp(-(dot(inputs,weights))))
	der=output*(1-output)
	err=outputs-output
	x=err*der
	weights=weights+dot(inputs.T,x)
print(weights)
print(1/(1+exp(-(dot(array([0,0]),weights)))))