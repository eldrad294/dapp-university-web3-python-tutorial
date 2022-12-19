class Vehicle{
    constructor(doors, passengerCapacity){
        this._doors = doors
        this._passengerCapacity = passengerCapacity
    }

    get doors(){
        return this._doors
    }

    get passengerCapacity(){
        return this._passengerCapacity
    }

    set doors(doors){
        this._doors = doors
    }

    set passengerCapacity(passengerCapacity){
        this._passengerCapacity = passengerCapacity
    }

    toString(){
        return "This vehicles has " + this._doors + " doors, " + this._passengerCapacity + " passenger capacity."
    }
}

vehicle = new Vehicle(4, 5, 5)
var newLine = "<br/>"
document.write(vehicle.doors)
document.write(newLine)
document.write(vehicle.passengerCapacity)
document.write(newLine)
document.write(vehicle.toString())
document.write(newLine)

class GroundVehicle extends Vehicle{
    constructor(doors, passengerCapacity, wheels){
        super(doors, passengerCapacity)
        this._wheels = wheels
    }

    get wheels(){
        return this._wheels
    }

    set wheels(wheels){
        this._wheels = wheels
    }

    toString(){
        return "This vehicles has " + this._wheels + " wheels," + this._doors + " doors, " + this._passengerCapacity + " passenger capacity."
    }
}

document.write("<hr/>")

groundVehicle = new GroundVehicle(4, 5, 5)
var newLine = "<br/>"
document.write(groundVehicle.wheels)
document.write(newLine)
document.write(groundVehicle.doors)
document.write(newLine)
document.write(groundVehicle.passengerCapacity)
document.write(newLine)
document.write(groundVehicle.toString())
document.write(newLine)

class Car extends GroundVehicle{
    constructor(doors, passengerCapacity, wheels, fuel){
        super(doors, passengerCapacity, wheels)
        this._fuel = new String(fuel)
    }

    get fuel(){
        return this._fuel
    }

    set fuel(fuel){
        this._fuel = fuel
    }

    toString(){
        return "This vehicles has " + this._wheels + " wheels," + this._doors + " doors, " + this._passengerCapacity + " passenger capacity, fuel " + this._fuel + "."
    }
}

document.write("<hr/>")

car = new Car(4, 5, 5, "Petrol")
var newLine = "<br/>"
document.write(car.wheels)
document.write(newLine)
document.write(car.doors)
document.write(newLine)
document.write(car.passengerCapacity)
document.write(newLine)
document.write(car.fuel)
document.write(newLine)
document.write(car.toString())
document.write(newLine)