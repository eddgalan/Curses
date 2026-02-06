export class Animal {
  constructor(public name: string) {}

  move() {
    console.log('moving...');
  }

  greetings() {
    return `Hello, I'm ${this.name}`;
  }
}

export class Dog extends Animal {
  constructor(name: string, public owner: string) {
    super(name);
    this.owner = owner;
  }

  woof(times: number = 1): void {
    for (let i = 0; i < times; i++) {
      console.log('Woof!');
    }
  }
}

const fifi = new Animal('Fifi');
fifi.move();
console.log(fifi.greetings());

const slinky = new Dog('Slinky', 'Edson');
slinky.move();
console.log(slinky.greetings());
slinky.woof(3);
console.log(`Owner: ${slinky.owner}`);
