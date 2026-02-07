export abstract class Animal {
  protected constructor(protected name: string) {}

  move() {
    console.log('moving...');
  }

  greetings() {
    return `Hello, I'm ${this.name}`;
  }

  protected doSomething(): void {
    console.log('Doing something...');
  }
}

export class Dog extends Animal {
  constructor(name: string, public owner: string) {
    super(name);
    this.owner = owner;
  }

  woof(times: number = 1): void {
    for (let i = 0; i < times; i++) {
      console.log(`Woof! ${this.name}`);
    }
    this.doSomething();
  }

  move(): void {
    console.log('Moving as a Dog');
    super.move();
  }
}

/*
const fifi = new Animal('Fifi');
fifi.move();
console.log(fifi.greetings());
 */

const slinky = new Dog('Slinky', 'Edson');
slinky.woof(2);
console.log(`Owner: ${slinky.owner}`);
slinky.move();
