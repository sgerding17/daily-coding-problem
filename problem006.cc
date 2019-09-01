// 2019-08-30
//
// An XOR linked list is a more memory efficient doubly linked list. Instead of
// each node holding next and prev fields, it holds a field named both, which
// is an XOR of the next node and the previous node. Implement an XOR linked
// list; it has an add(element) which adds the element to the end, and a
// get(index) which returns the node at index.

#include <assert.h>
#include <iostream>
#include <memory>

using namespace std;

struct node_t
{
    int element {0};
    node_t *both {nullptr};
};

node_t *x(node_t *a, node_t *b)
{
    return reinterpret_cast<node_t*>(
               reinterpret_cast<uint64_t>(a) ^
               reinterpret_cast<uint64_t>(b));
}

class node_itr
{
public:
    node_itr() {}

    static node_itr create_from_prev(node_t *self, node_t *prev)
    {
        return node_itr(self,
                        prev,
                        self ? x(self->both, prev) : nullptr);
    }
    static node_itr create_from_next(node_t *self, node_t *next)
    {
        return node_itr(self,
                        self ? x(self->both, next) : nullptr,
                        next);
    }

    operator bool()
    {
        return self != nullptr;
    }

    bool operator==(const node_itr &other)
    {
        return self == other.self;
    }

    int get_element()
    {
        return self->element;
    }

    node_itr get_next()
    {
        return node_itr::create_from_prev(next, self);
    }

    node_itr get_prev()
    {
        return node_itr::create_from_next(prev, self);
    }

    node_itr append(const int element)
    {
        node_t *new_node = new node_t;
        new_node->element = element;

        next = new_node;
        self->both = x(prev, next);
        new_node->both = self;

        return node_itr::create_from_prev(new_node, self);
    }

private:
    node_itr(node_t *_self,
             node_t *_prev,
             node_t *_next) :
        self(_self),
        prev(_prev),
        next(_next)
    {}

    node_t *self {nullptr};
    node_t *prev {nullptr};
    node_t *next {nullptr};
};

class list
{
public:
    void add(const int element)
    {
        if (!tail)
        {
            node_t *new_node = new node_t;
            new_node->element = element;
            head = tail = node_itr::create_from_next(new_node, nullptr);
        }
        else if (head == tail)
        {
            tail = head.append(element);
        }
        else
        {
            tail = tail.append(element);
        }
    }

    node_itr get(const size_t index)
    {
        node_itr retval = head;
        for (size_t i = 0; i < index; i++)
        {
            if (!retval) break;
            retval = retval.get_next();
        }
        return retval;
    }

private:
    node_itr head;
    node_itr tail;
};

int main()
{
    list l;
    assert(!l.get(0));
    for (size_t i = 0; i < 10; i++)
    {
        l.add(i + 100);

        for (size_t j = 0; j <= i; j++)
        {
            assert((bool)l.get(j));
            assert(l.get(j).get_element() == j + 100);
        }
        for (size_t j = i + 1; j < 10; j++)
        {
            assert(!l.get(j));
        }
    }

    assert(l.get(7).get_prev().get_prev().get_element() == 105);

    return 0;
}

//    node_t *head = new node_t;
//    head->element = 1;
//
//    node_itr itr = node_itr::create_from_prev(head, nullptr);
//    for (int element = 2; element <= 10; element++)
//    {
//        cout << "Appending " << element << endl;
//        itr = itr.append(element);
//    }
//
//    cout << endl;
//
//    for (; itr; itr = itr.get_prev())
//    {
//        cout << itr.get_element() << endl;
//    }
//
//    cout << endl;
//
//    for (node_itr i = node_itr::create_from_prev(head, nullptr);
//         i;
//         i = i.get_next())
//    {
//        cout << i.get_element() << endl;
//    }
//
//    cout << (bool)l.get(0) << endl;
//    cout << (bool)l.get(1) << endl;
//    cout << (bool)l.get(2) << endl;
//    assert(!l.get(0));
//    assert(!l.get(1));
//    assert(!l.get(2));
//
//    l.add(10);
//    cout << (bool)l.get(0) << endl;
//    cout << (bool)l.get(1) << endl;
//    cout << (bool)l.get(2) << endl;
//    cout << l.get(0).get_element() << endl;
//    assert(l.get(0).get_element() == 10);
//    assert(!l.get(1));
//    assert(!l.get(2));
//
//    l.add(20);
//    cout << (bool)l.get(0) << endl;
//    cout << (bool)l.get(1) << endl;
//    cout << (bool)l.get(2) << endl;
//    cout << l.get(0).get_element() << endl;
//    cout << l.get(1).get_element() << endl;
//    assert(l.get(0).get_element() == 10);
//    assert(l.get(1).get_element() == 20);
//    assert(!l.get(2));

//struct forward_xor_node_t
//{
//    forward_xor_node_t(xor_node_t *_self,
//                       xor_node_t *_prev) :
//        self(_self),
//        prev(_prev)
//    {}
//    xor_node_t *self;
//    xor_node_t *prev;
//
//    bool at_end() const
//    {
//        return self == nullptr;
//    }
//    forward_xor_node_t get_next() const
//    {
//        xor_node_t *next = x(self->both, prev);
//        return forward_xor_node_t(next, self);
//    }
//    forward_xor_node_t append(const int value)
//    {
//        xor_node_t *new_node = new xor_node_t;
//        new_node->value = value;
//
//        self->both = x(prev, new_node);
//        new_node->both = self;
//
//        return forward_xor_node_t(new_node, self);
//    }
//};
//
//struct reverse_xor_node_t
//{
//    reverse_xor_node_t(xor_node_t *_self,
//                       xor_node_t *_next) :
//        self(_self),
//        next(_next)
//    {}
//    xor_node_t *self;
//    xor_node_t *next;
//
//    bool at_begin() const
//    {
//        return self == nullptr;
//    }
//    reverse_xor_node_t get_prev() const
//    {
//        xor_node_t *prev = x(self->both, next);
//        return reverse_xor_node_t(prev, self);
//    }
//};




//    forward_xor_node_t tail_itr(head, nullptr);
//    for (int i = 0; i < 10; i++)
//    {
//        const int value = i+1;
//        cout << "Inserting " << value << endl;
//        tail_itr = tail_itr.append(value);
//    }
//
//    xor_node_t *tail = tail_itr.self;
//
//    for (forward_xor_node_t itr(head, nullptr);
//         !itr.at_end();
//         itr = itr.get_next())
//    {
//        cout << itr.self->value << endl;
//    }
//    
//    cout << endl;
//
//    for (reverse_xor_node_t itr(tail, nullptr);
//         !itr.at_begin();
//         itr = itr.get_prev())
//    {
//        cout << itr.self->value << endl;
//    }

//struct node_t
//{
//    int value {0};
//    shared_ptr<node_t> prev {nullptr};
//    shared_ptr<node_t> next {nullptr};
//};
//
//shared_ptr<node_t> append(shared_ptr<node_t> node, const int value)
//{
//    shared_ptr<node_t> new_node(new node_t);
//    new_node->value = value;
//
//    node->next = new_node;
//    new_node->prev = node;
//
//    return new_node;
//}

//    shared_ptr<node_t> head(new node_t);
//    shared_ptr<node_t> tail(head);
//    for (int i = 0; i < 10; i++)
//    {
//        tail = append(tail, i+1);
//    }
//
//    for (shared_ptr<node_t> n = head; n != nullptr; n = n->next)
//    {
//        cout << n->value << endl;
//    }
//
//    for (shared_ptr<node_t> n = tail; n != nullptr; n = n->prev)
//    {
//        cout << n->value << endl;
//    }


//        xor_node_t *new_node = new xor_node_t;
//        new_node->value = i+1;
//
//        tail_itr.self->both = x(tail_itr.prev, new_node);
//        new_node->both = tail_itr.self;
//
//        tail_itr = forward_xor_node_t(new_node, tail_itr.self);
