public class BinaryTree {
    private Node root = null;
    private Node left = null;
    private Node right = null;

    public BinaryTree(){}
    public BinaryTree(Node root){
        this.root = root;
    }

    public void insert(int x){
        Node t = new Node(x);
        //TODO: Create insertion and look into implementing balancing
    }

    public class Node {
        private final int val;
        private Node next_node = null;

        public Node(int x) {
            this.val = x;
        }

        public int getVal(){return this.val;}
        public void setNode(Node node){this.next_node = node;}
        public Node getNext_node(){return this.next_node;}
    }

    public static void main(String[] args) {
        System.out.println("Hello World");
    }
}
