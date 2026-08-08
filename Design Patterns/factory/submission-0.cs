public interface IVehicle {
    string getType();
}

public class Car : IVehicle {
    public string getType() {
        return "Car";
    }
}

public class Bike : IVehicle {
    public string getType() {
        return "Bike";
    }
}

public class Truck : IVehicle {
    public string getType() {
        return "Truck";
    }
}

public abstract class VehicleFactory {
    public abstract IVehicle createVehicle();
}

public class CarFactory : VehicleFactory {
    public override Car createVehicle(){
        return new Car();
    }
}

public class BikeFactory : VehicleFactory {
    public override Bike createVehicle(){
        return new Bike();
    }
}

public class TruckFactory : VehicleFactory {
    public override Truck createVehicle(){
        return new Truck();
    }
}
