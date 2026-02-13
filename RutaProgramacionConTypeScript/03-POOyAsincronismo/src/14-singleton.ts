export class MyService {
  static instance: MyService | null = null;

  private constructor(public name: string) {}

  getName() {
    return this.name;
  }

  static create(name: string): MyService {
    if (!MyService.instance) {
      console.log('Creating new instance...');
      MyService.instance = new MyService(name);
    }
    return MyService.instance;
  }
}

const myService = MyService.create('Service 1');
console.log(myService.getName());

const myService2 = MyService.create('Service 2');
console.log(myService2.getName());

const myService3 = MyService.create('Service 2');
console.log(myService3.getName());

console.log(myService === myService2);
