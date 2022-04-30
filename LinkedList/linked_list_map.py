class LinkedList {
  constructor()
  {
      this.head = null;
  }

  fromArray(arr) {
    let curr = null;
    console.log(curr)
    arr.forEach((val) => {
      if (this.head == null) {
        this.head = new ListNode(val);
        curr = this.head;
      } else {
        let newNext = new ListNode(val);
        curr.next = newNext;
        curr = newNext;
      }
    });
  }

}
class ListNode {
  // constructor
  constructor(value)
  {
      this.value = value;
      this.next = null
  }
}

function mapper(value){
  return 2 * new ListNode(value)
}

function map(node, mapper){
  result = new LinkedList
  while (node){
    mapped_node = mapper(node.value)
    if (result.head == null){
      result.head = mapped_node
      curr = result.head
    } else {
      let newNext = mapped_node
      curr.next = newNext;
      curr = newNext;
    }  
    node = node.next
    // curr = node.next
  }
  return result
  // if head is null
    //.   create new mapped_head
    //.   set curr as head
    // else
    //    create new node
    //.   assign new node to curr.next
    //    set new node to curr
}

let LL1 = new LinkedList(1)

console.log(map(LL1, mapper))
