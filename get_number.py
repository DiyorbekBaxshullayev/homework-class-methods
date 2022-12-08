class Numbers:
    def __init__(self,get_number):
        self.get_number=get_number

    def is_even(self):
        if self.get_number%2==0:
            return True
        else:
            return False
    def is_odd(self):
        if self.get_number%2==1:
            return True
        return False
    def is_prime(self):
        a=[]
        for i in range(1,self.get_number+1):
            if self.get_number%i==0:
                a.append(i)
        if len(a)<=2:
            return True
        else:
            return False
    def get_divisors(self):
        b=[]
        for i in range(1,self.get_number+1):
            if self.get_number%i==0:
                b.append(i)
        return b
    def get_length(self):
        return len(str(self.get_number))
    def get_sum(self):
        d=0
        for i in str(self.get_number):
            d+=int(i)
        return d
    def get_product(self):
        e=[]
        for i in str(self.get_number):
            e.append(i)
        return e
    def get_reverse(self):
        f=[]
        g=[]
        for i in str(self.get_number):
            f.append(i)
            g=f[-1::-1]
            a=''
            for l in g:
                a+=l
        return int(a)
    def get_digits(self):
        a=list(str(self.get_number))
        return a
    def get_max(self):
        a=list(str(self.get_number))
        max=0
        for i in a:
            if int(i)>max:
                max=int(i)
        return max
    def get_min(self):
        a=list(str(self.get_number))
        min=int(a[0])
        for i in a:
            if int(i)<min:
                min=int(i)
        return min
    def get_average(self):
        a=0
        b=0
        for i in list(str(self.get_number)):
            a+=int(i)
            b+=1
        return a/b


x=Numbers(get_number=854)
print(x.get_number)
print(x.is_even())
print(x.is_odd())
print(x.is_prime())
print(x.get_divisors())
print(x.get_length())
print(x.get_sum())
print(x.get_product())
print(x.get_reverse())
print(x.get_digits())
print(x.get_max())
print(x.get_min())
print(x.get_average())