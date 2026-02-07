interface Driver {
  database: string;
  password: string;
  port: number;

  connect(): void;
  disconnect(): void;
  isConnected(): boolean;
}

/*
const driver: Driver = {
  database: 'my_database',
  password: '12345678a',
  port: 3306
};
*/

class PostgresDriver implements Driver {
  constructor(
    public database: string,
    public password: string,
    public port: number
  ) {}

  connect(): void {
    console.log('Connected to Postgres');
  }

  disconnect(): void {
    console.log('Disconnected from Postgres');
  }

  isConnected(): boolean {
    return true;
  }
}

class MySQLDriver implements Driver {
  constructor(
    public database: string,
    public password: string,
    public port: number
  ) {}

  connect(): void {
    console.log('Connected to MySQL');
  }

  disconnect(): void {
    console.log('Disconnected from MySQL');
  }
  isConnected(): boolean {
    return false;
  }
}
