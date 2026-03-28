def create_node(data):
    return {"data": data, "next": None}

def insert_at_beginning(head, data):
    new_node = create_node(data)
    new_node["next"] = head
    return new_node

def insert_at_end(head, data):
    new_node = create_node(data)
    if head is None:
        return new_node
    temp = head
    while temp["next"] is not None:
        temp = temp["next"]
    temp["next"] = new_node
    return head

def traverse(head):
    temp = head
    while temp is not None:
        print(temp["data"], end=" -> ")
        temp = temp["next"]
    print("None")

head = None
head = insert_at_beginning(head, 10)
head = insert_at_beginning(head, 20)
head = insert_at_end(head, 30)
traverse(head)
