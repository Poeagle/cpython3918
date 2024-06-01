#include <pybind11/pybind11.h>

namespace py = pybind11;

// 一个简单的函数
int add(int i, int j) {
    return i + j;
}

// 一个简单的类
class Pet {
public:
    Pet(const std::string &name) : name(name) {}

    void setName(const std::string &name) {
        this->name = name;
    }

    std::string getName() const {
        return name;
    }

private:
    std::string name;
};

// 绑定代码
PYBIND11_MODULE(example, m) {
    m.doc() = "pybind11 example plugin"; // 可选模块文档字符串

    // 暴露add函数
    m.def("add", &add, "A function which adds two numbers");

    // 暴露Pet类
    py::class_<Pet>(m, "Pet")
        .def(py::init<const std::string &>())
        .def("setName", &Pet::setName)
        .def("getName", &Pet::getName);
}

