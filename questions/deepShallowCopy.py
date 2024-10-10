
import copy

x =[1,3,4]
y=copy.copy(x)
z= copy.deepcopy(x)
print(y is z)

del x[0]
print(x)
print(y)
print(z)

# for more details : https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.codingninjas.com%2Fcodestudio%2Flibrary%2Fexplain-the-difference-between-shallow-copy-and-deep-copy&psig=AOvVaw0wRiBjwp_tOXKaowfKGbH8&ust=1681151687392000&source=images&cd=vfe&ved=0CBEQjRxqFwoTCMCGqcW4nf4CFQAAAAAdAAAAABAD




