import Vue from 'vue';
import Router from 'vue-router';
import Groceries from './components/Groceries.vue';
import Ping from './components/Ping.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Groceries',
      component: Groceries,
    },
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
  ],
});
