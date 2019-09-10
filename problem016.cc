// 2019-09-09
//
// You run an e-commerce website and want to record the last N order ids in a
// log. Implement a data structure to accomplish this, with the following API:
//
// record(order_id): adds the order_id to the log
// get_last(i): gets the ith last element from the log. i is guaranteed to be
// smaller than or equal to N..

#include <array>
#include <assert.h>

using namespace std;

using order_id_t = int;

template<size_t N>
class OrderLog
{
public:
    void record(const order_id_t order_id)
    {
        ids[next] = order_id;
        next = (next + 1) % ids.size();
    }

    order_id_t get_last(const size_t i) const
    {
        return ids[(ids.size() + next - 1 - i) % ids.size()];
    }

private:
    array<order_id_t, N> ids {};
    size_t next {0u};
};

int main()
{
    OrderLog<3> log;
    
    log.record(1);
    log.record(2);
    log.record(3);

    assert(log.get_last(0) == 3);
    assert(log.get_last(1) == 2);
    assert(log.get_last(2) == 1);

    log.record(4);

    assert(log.get_last(0) == 4);
    assert(log.get_last(1) == 3);
    assert(log.get_last(2) == 2);

    log.record(5);
    log.record(6);

    assert(log.get_last(0) == 6);
    assert(log.get_last(1) == 5);
    assert(log.get_last(2) == 4);

    return 0;
}
