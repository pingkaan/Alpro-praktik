#include <iostream> 
using namespace std;
  
int main()
{
  cout << "=== Penjumlahan Deret ===" << endl;
  cout << "=====================================" << endl;
  cout << endl;
   
  int i, n, total, rata;
   
  cout << "Jumlah deret yang di inginkan: ";
  cin >> n;
  cout << endl;
   
  total = 0;
  cout<<"Deret bilangan genap"<<endl;
  for (i = 1; i <= n; i++) {
  	  cout << i * 2 << "  ";
      total = total + i*2;
  }
  cout<<"\n\nPenjumlahan deret bilangan"<<endl;
  for (i = 1; i <= n; i++) {
  	 cout << i * 2 << " + ";
      total = total + i*2;
  }
  cout << " = " << total;
  
  rata=total/n;
  cout<<"\n\nRata-rata : "<<rata;
   
  cout << endl;
  return 0;
}
