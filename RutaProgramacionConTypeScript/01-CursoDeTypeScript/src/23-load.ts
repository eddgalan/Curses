// var _ = require('lodash');   // Importación según la doc de la librería

import _ from 'lodash';

const data = [
  {
    username: 'edson',
    role: 'admin',
  },
  {
    username: 'juan',
    role: 'seller',
  },
  {
    username: 'fernando',
    role: 'admin',
  },
  {
    username: 'santiago',
    role: 'customer',
  }
];

const response = _.groupBy(data, (item) => item.role);
console.log(response);
