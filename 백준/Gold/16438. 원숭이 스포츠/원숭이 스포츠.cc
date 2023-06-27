#include <iostream>
#include <vector>

using namespace std;

vector<string> games;
bool flag = false;

void organization(int layer, int start, int end)
{
	if (layer == 7)
		return;
	int mid = (start + end) / 2;

	for (int i = start; i < mid; i++)
		games[layer] += 'A';
	for (int i = mid; i < end; i++)
		games[layer] += 'B';

	organization(layer + 1, start, mid);
	organization(layer + 1, mid, end);
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	int N;
	cin >> N;
	string s = "";
	string temp = "";
	for (int i = 0; i < 7; i++)
		games.push_back("");
	organization(0, 0, N);
	for (int i = 0; i < N; i++)
	{
		s += 'B';
		if (i == 0)
			temp += 'A';
		else
			temp += 'B';
	}

	for (int i = 0; i < 7; i++)
	{
		if (games[i] == s)
			cout << temp << endl;
		else
			cout << games[i] << endl;
	}
}