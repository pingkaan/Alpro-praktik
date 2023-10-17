import matplotlib.pyplot as plt

data = [100,53,84,64,72,73,73,45,86,50,60,58]
month = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

plt.title("Penjualan Mobil Perbulan")
plt.plot(month,data,alpha=0.5)
plt.scatter(range(12),data,color="red")

plt.show()