#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

struct Task
{
	int st, dur, price;
	bool operator<(const Task &t) const
	{
		return st <t.st;
	}
	bool operator<(const int a) const
	{
		return st <a;
	}
};

//for ( ; j >= 0 && vt[j].st + vt[j].dur > vt[i].st; j--);Logic error
int tasksPicker(vector<Task> &vt)
{
	vector<int> prices(vt.size()+1);
	prices[vt.size()-1] = vt[vt.size()-1].price;
	for (int i = vt.size()-2; i >= 0 ; i--)
	{
		int j=lower_bound(vt.begin()+i+1,vt.end(),vt[i].st+vt[i].dur)-vt.begin();
		prices[i] = max(prices[i+1], vt[i].price+prices[j]);
	}
	return prices[0];
}

void RentyourAirplaneandmakeMoney()
{
	int T = 0, n = 0, cap;
	cin>>T;
	while (T--)
	{
		cin>>n;
		vector<Task> vt(n);
		cap = 0;
		for (int i = 0; i <n; i++)
		{
			cin>>vt[i].st>>vt[i].dur>>vt[i].price;
			cap = max(cap, vt[i].st + vt[i].dur);
		}
		sort(vt.begin(), vt.end());
		cout<<tasksPicker(vt)<<endl;
	}
}

int main()
{
	RentyourAirplaneandmakeMoney();
	return 0;
}