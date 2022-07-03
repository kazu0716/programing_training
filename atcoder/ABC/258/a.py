K = int(input())
h, m = K//60, K % 60
print(f"{21+h}:{str(0+m).zfill(2)}")
