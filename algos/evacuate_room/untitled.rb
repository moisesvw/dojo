class Node
  attr_accessor :value, :next

  def initialize(value)
    @value = value
  end
end

class LinkedList
  attr_accessor :head, :tail

  def initialize
    @head = nil
    @tail = nil
  end

  def empty?
    head.nil?
  end

  def to_s
    puts walk.to_s
  end

  def walk
    node = head
    elements = []
    while node != nil
      elements.push node.value
      node = node.next
    end
    
    elements
  end

  def add(value)
    n = Node.new(value)
    if head.nil?
      self.head = n
      self.tail = n
    else
      tail.next = n
      self.tail = n
    end
  end
end

l = LinkedList.new
l.add(5)
l.add(6)
l.add(8)
l.tail
l.head