public class DynamicArray {
    private int[] _items;
    private int _capacity;
    private int _size;

    public DynamicArray(int capacity) {
        this._items = new int[capacity];
        Console.WriteLine(this._items[0]);
        this._capacity = capacity;
        this._size = 0;
    }

    public int Get(int i) {
        return this._items[i];
    }

    public void Set(int i, int n) {
        this._items[i] = n;
    }

    public void PushBack(int n) {
        Console.WriteLine("hello");
        if (GetSize() >= GetCapacity()){
            this.Resize();
        }
        this._items[GetSize()] = n;
        this._size++;
    }

    public int PopBack() {
        var result = this._items[GetSize() - 1];
        this._items[GetSize() - 1] = 0;
        this._size--;
        return result;
    }

    private void Resize() {
        this._capacity *= 2;
        Console.WriteLine(GetCapacity());
        int[] new_items = new int[this._capacity];
        for (int i = 0; i < this._size; i++){
            new_items[i] = this._items[i];
        }
        this._items = new_items;
    }

    public int GetSize() {
        return this._size;
    }

    public int GetCapacity() {
        return this._capacity;
    }
}
