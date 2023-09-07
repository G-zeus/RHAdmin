import {createRouter, createWebHashHistory} from 'vue-router'


const routes = [
  {
    path: '/login',
    name: 'login',
    component: () => import('@/modules/auth/pages/Login.vue')
  },
  {
    path: '/',
    component: () => import('@/modules/auth/pages/Login.vue')
  },
  {
    path: '/dashboard',
    name: 'dashboard',
    component: () => import('@/modules/dashboard/pages/Dashboard.vue')
  },
  {
    path: '/nuevoEmpleado',
    name: 'nuevoEmpleado',
    component: () => import('@/modules/dashboard/pages/New.vue')
  },
  {
    path: '/editarEmpleado/:id',
    name: 'editarEmpleado',
    component: () => import('@/modules/dashboard/pages/Edit.vue')
  },
  {
    path: '/infoEmergencia/:id',
    component: () => import('@/modules/emergency/pages/Info.vue')
  },
  {
    path: '/:pathMatch(.*)*',
    component: () => import('@/modules/common/pages/NotFound')
  },

]


const router = createRouter({
  // 4. Provide the history implementation to use. We are using the hash history for simplicity here.
  history: createWebHashHistory(),
  routes, // short for `routes: routes`
})


export default router
