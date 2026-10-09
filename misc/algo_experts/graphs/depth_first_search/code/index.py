r"""TODO: port to Python.

Original JavaScript (misc/algo-experts/graphs/depth-first-search/code/index.js):

class Node {
    constructor(name) {
        this.name = name;
        this.children = [];
    }

    addChild(name) {
        this.children.push(new Node(name));
        return this;
    }

    depthFirstSearch(array) {
        // console.log('array');
        // console.log(array);

        array.push(this.name);

        for (const child of this.children) {
            child.depthFirstSearch(array);
        }

        return array;
    }
}

exports.Node = Node;

"""
