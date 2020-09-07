#!/usr/bin/env python
# coding: utf-8

# # 1.

# In[38]:


def Factorial(n): #Definimos la función factorial.
    if n%1!=0: #Nos cercioramos de que el número ingresado sea entero.
        return("Ingrese un número entero")
    else:
        if n==0:
            return(1)
        else:
            prod=1
            for i in range(1,n+1): #Abrimos un ciclo para la productoria de elementos.
                prod*=i
            return(int(prod)) #Retornamos un número entero.
        


# # 2.

# In[118]:


def Binomial(n,k): #Definimos la función binomial.
    if n%1!=0 or k%1!=0: #Nos aseguramos de que sean números enteros.
        return("Ingrese números enteros.")
    else:
        return int(Factorial(n)/(Factorial(k)*Factorial(n-k))) #Retornamos un resultado entero.


# # 3.

# In[151]:


def Pascal(n):
    pascal=open('Pascal-%i.txt'%n,'w') #Abrimos archivo txt.
    i=0 #Inicializamos variables.
    a=1
    for t in range(n): 
        if t+1==10**a: #Cuando haya un aumento de cifras en n, se correrán las filas de modo que la primera
            pascal.write("n=%i"%(t+1)) #diagonal quedé recta y escribimos sobre el archivo txt los números 
            pascal.write(" "*(n-i+5-a)) #números correspondientes.
            a+=1
            i+=1
        else:
            pascal.write("n=%i"%(t+1))
            pascal.write(" "*(n-i+5))
        for j in range(t+1):
            pascal.write(str(Binomial(t,j)))
            pascal.write(" ")
        i+=1
        pascal.write("\n") #Se pasa a la siguiente fila.
    pascal.close()
            
        


# In[152]:





# # 4.

# In[154]:


def Probabilidad(n,k): #Definimos la función de probabilidad.
    return (Binomial(n,k))/2**n 


# ## a)

# In[155]:


Probabilidad(100,10) 


# ## b)

# In[150]:


pros=[]
for i in range(30,101):
    pros.append(Probabilidad(100,i))
    
suma=0
for i in pros:
    suma+=i

print("La probabilidad de que de que caiga cara o sello más de treinta veces en 100 intentos es:%f"%(suma))
    
    

