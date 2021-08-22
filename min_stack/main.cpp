//
// Created by Jacob on 8/20/2021.
//
#include <iostream>
#include <stdexcept>

#include "main.h"

class MinStack {
public:
    /** initialize your data structure here. */
    // implementation:
    // Doubly linked list that tracks head, tail, max and min nodes

    MinStack() {
        throw std::logic_error("Not implemented")
    }

    void push(int val) {
        throw std::logic_error("Not implemented")
    }

    void pop() {
        throw std::logic_error("Not implemented")
    }

    int top() {
        throw std::logic_error("Not implemented")
    }

    int getMin() {
        throw std::logic_error("Not implemented")
    }
};

int main(argc, argv[]){
    MinStack* obj = new MinStack();
    for(int i = -5; i < 5; i++){
        obj->push(i);
    }
    obj->pop();
    int param_3 = obj->top();
    int param_4 = obj->getMin();
}

// TODO: https://www.jetbrains.com/help/clion/unit-testing-tutorial.html#google-test-framework