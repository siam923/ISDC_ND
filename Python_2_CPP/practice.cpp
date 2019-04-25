#include "helpers.h"
#include <iostream>
#include <vector>
using namespace std;

int main()
{
  	vector < vector<float> > matrix(5, vector<float> (3, .4));
  	vector <vector<float> > norm = normalize(matrix);
  	
  	for(int i=0; i<norm.size();i++){
    	for(int j=0;j<norm[0].size();j++){
        	cout<< norm[i][j] <<" ";
        }
      cout << endl;
    }
  
	return 0;
}