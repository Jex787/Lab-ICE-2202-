#include <iostream>
#include <queue>
using namespace std;

class Queue
{
private:
    queue<int> q;

public:
    void enqueue(int value)
    {
        q.push(value);
    }

    void dequeue()
    {
        if (!q.empty())
        {
            q.pop();
        }
        else
        {
            cout << "Queue is empty." << endl;
        }
    }

    int front()
    {
        if (!q.empty())
        {
            return q.front();
        }
        else
        {
            cout << "Queue is empty." << endl;
            return -1;
        }
    }

    int size()
    {
        return q.size();
    }

    bool is_empty()
    {
        return q.empty();
    }
};

int main()
{
    Queue q;

    // Enqueue elements
    q.enqueue(1);
    q.enqueue(2);
    q.enqueue(3);

    // Print front element
    cout << "Front element: " << q.front() << endl;

    // Dequeue elements
    q.dequeue();
    q.dequeue();

    // Print size of the queue
    cout << "Size of the queue: " << q.size() << endl;

    // Check if queue is empty
    cout << "Is queue empty? " << (q.is_empty() ? "Yes" : "No") << endl;

    return 0;
}
